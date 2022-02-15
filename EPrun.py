


import sys
sys.path.insert(0, 'C:/EnergyPlusV9-5-0')
from pyenergyplus.api import EnergyPlusAPI
api = EnergyPlusAPI()

import numpy as np
from ray.rllib.env.external_env import ExternalEnv
from IDF_tool import Schedules, LocationClimate, MainFunctions


class EPsimulator:
    
    def decimal_a_lista(decimal, len):
        '''
        Esta función transforma una acción del espacio de acciones (entero) a una lista de longitud 
        asignada que contiene el valor binario del entero. 
        '''
        global EPconfig
        # se comprueba que el entero se pueda representar como un binario de la longitud asignada
        if decimal >= 2**len:
            return print("Error: decimal out of range.")
        # se comprueba que el entero sea positivo
        if decimal < 0:
            return print("Error: decimal out of range.")
        # si el entero es 0, entonces el binario es una lista de la longitud especificada llena de ceros.
        if decimal == 0:
            binario = []
            i=0
            while i <= len-1:
                binario.append(0)
                i+=1
            return binario

    def episode_epJSON(conf_experimento, month, day):
        """
        Este toma un archivo epJSON y lo modifica. Luego retorna la ruta del archivo modificado.
        Las modificaciones efectuadas son:
            1. Cambio del mes a ejecutar.
            2. Cambio del día a ejecutar.
            3. Cambio en los path de los calendarios de disponibilidad de los objetos accionables en la vivienda.
        """
        global EPconfig
        epJSON_file_old = MainFunctions.MainFunctions.read_epjson(conf_experimento['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        LocationClimate.RunPeriod.begin_day_of_month(epJSON_file_old, "DDMM", day)
        LocationClimate.RunPeriod.begin_month(epJSON_file_old, "DDMM", month)
        LocationClimate.RunPeriod.end_day_of_month(epJSON_file_old, "DDMM", day)
        LocationClimate.RunPeriod.end_month(epJSON_file_old, "DDMM", month)
        Schedules.Schedule_File.file_name(epJSON_file_old, "Aviability_Control", conf_experimento['directorio'] + '/Resultados/RL_Aviability_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "Shadow_Control", conf_experimento['directorio'] + '/Resultados/RL_Control_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "VentN_Control", conf_experimento['directorio'] + '/Resultados/VentN_Aviability_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "VentS_Control", conf_experimento['directorio'] + '/Resultados/VentS_Aviability_Sch_0.csv')
        MainFunctions.MainFunctions.write_epjson(conf_experimento['directorio'] + '/Resultados/new.epJSON', epJSON_file_old)
        epJSON_new = conf_experimento['directorio'] + '/Resultados/new.epJSON'

        return epJSON_new

    def EP_exchange_function(state):
        '''
        # Callback function for EnergyPlus

        Este método permite el intercambio de información (entrada y salida) entre el simulador
        EnergyPlus y un ejecutor de decisiones. El objeto de la creación de este método es poder 
        realizar aprendizaje automático sobre las decisiones de un edificio a partir de la utilización
        de aprendizaje por refuerzos.
        '''
        # The variables of the experiment, case and episode can not be called in the method's variables
        # and due that are called here as global variables.
        # conf_experimento are those which no change in all the run. var_case_n are those which change only
        # between configurations (ej. the learning rate tuning). var_step_t are those which change inside the
        # episode by step times.
        global first_time_step
        global EPconfig
        
        #Condición necesaria para leer las variables disponibles en EP a solicitar
        if api.exchange.api_data_fully_ready(state):
            
            #Condición para que no se escriban los datos durante el periodo de calentamiento
            if api.exchange.warmup_flag(state) == 0:
                
                """
                LECTURA DE VARIABLES DE ESTADO (s_tp1)
                """
                '''Lectura de algunas variables'''
                # num_time_steps_in_hour is used to compute the n-step_max in a episode and the quantity of
                # minutes of comfort
                num_time_steps_in_hour = api.exchange.num_time_steps_in_hour(state)
                # time_step and hour are needed to obtain the radiation rad
                # time step is based on data of EP and is in range between one hour
                time_step = api.exchange.zone_time_step_number(state)
                hour = api.exchange.hour(state)

                '''Lectura de los handles'''
                # Handles are needed before call the values that are inside them.
                # hadle for the radiation in the plane of the windows
                Bw_handle = api.exchange.get_variable_handle(state, "Surface Outside Face Incident Solar Radiation Rate per Area", "Zn001:Wall001:Win001")
                # handle for the outside temperature
                To_handle = api.exchange.get_variable_handle(state, "Site Outdoor Air Drybulb Temperature", "Environment")
                # hadle for the inside (zone) temperature
                Ti_handle = api.exchange.get_variable_handle(state, "Zone Mean Air Temperature", "Thermal Zone: Modelo_Simple")
                # handle for wind speed in the site
                v_handle = api.exchange.get_variable_handle(state, "Site Wind Speed", "Environment")
                # handle for direction of the wind
                d_handle = api.exchange.get_variable_handle(state, "Site Wind Direction", "Environment")
                # handle for the inside relativ humidity
                RHi_handle = api.exchange.get_variable_handle(state,"Zone Air Relative Humidity", "Thermal Zone: Modelo_Simple")

                '''Lectura de las variables de estado'''
                # Here the values of the handles are consulting
                rad = api.exchange.today_weather_beam_solar_at_time(state, hour, time_step)
                Bw = api.exchange.get_variable_value(state, Bw_handle)
                To = api.exchange.get_variable_value(state, To_handle)
                Ti = api.exchange.get_variable_value(state, Ti_handle)
                v = api.exchange.get_variable_value(state, v_handle)
                d = api.exchange.get_variable_value(state, d_handle)
                RHi = api.exchange.get_variable_value(state, RHi_handle)
                
                # the values are saved in a dictionary to compose the observation (or state)
                s_cont_tp1 = np.array([rad,Bw,To,Ti,v,d,RHi])
                EPconfig['last_observation'].update(s_cont_tp1)

                """
                CÁLCULO DE ENERGÍA, CONFORT Y RECOMPENSA
                """
                # handle for the energy consumption for cooling
                q_supp_handle = api.exchange.get_meter_handle(state, 'Cooling:DistrictCooling')
                q_supp = api.exchange.get_meter_value(state, q_supp_handle)

                # The energy consumption e is equal to the q_supp value but in kWh not in J
                e_tp1 = q_supp/(3.6*1000000)

                #La recompensa es calculada a partir de la energía y los minutos de confort
                if Ti > EPconfig['T_SP'] + EPconfig['dT_up'] or Ti < EPconfig['T_SP'] - EPconfig['dT_dn']:
                    if RHi > EPconfig['SP_RH']:
                        r_temp = - EPconfig['rho']*(Ti - EPconfig['T_SP'])**2
                        r_hr = - EPconfig['psi']*(RHi - EPconfig['SP_RH'])**2
                    else:
                        r_temp = - EPconfig['rho']*(Ti - EPconfig['T_SP'])**2
                        r_hr = EPconfig['psi'] * 10

                elif RHi > EPconfig['SP_RH']:
                    r_temp = EPconfig['rho'] * 10
                    r_hr = - EPconfig['psi']*(RHi - EPconfig['SP_RH'])**2

                else:
                    r_temp = EPconfig['rho'] * 10
                    r_hr = EPconfig['psi'] * 10
                
                if e_tp1 > 0:
                    r_energia = - EPconfig['beta']*e_tp1
                else:
                    r_energia = EPconfig['beta']
                
                r_tp1 = r_energia + r_temp + r_hr

                """
                SE GRABAN LAS VARIABLES PARA EL TIEMPO t
                """
                if first_time_step == False:
                    ExternalEnv.log_returns(ExternalEnv, EPconfig['episode'], r_tp1, {}, {})

                """Se obtiene la acción de RLlib"""
                a_tp1 = ExternalEnv.get_action(ExternalEnv, EPconfig['episode'], s_cont_tp1)
                
                """
                SE REALIZAN LAS ACCIONES EN EL SIMULADOR
                """
                '''Se solicitan los handles de cada una de las variables que se quiere controlar'''
                # handle para el control de la persiana
                ShadingControlHandle = api.exchange.get_actuator_handle(state, 'Schedule:File', 'Schedule Value', 'Shadow_Control')
                # handle para el control del aire acondicionado
                HVACControlHandle = api.exchange.get_actuator_handle(state, 'Schedule:File', 'Schedule Value', 'Aviability_Control')
                # handle para el control de abertura de la ventana orientada al norte
                VentN_ControlHandle = api.exchange.get_actuator_handle(state, 'Schedule:File', 'Schedule Value', 'VentN_Control')
                # handle para el control de abertura de la ventana orientada al sur
                VentS_ControlHandle = api.exchange.get_actuator_handle(state, 'Schedule:File', 'Schedule Value', 'VentS_Control')
                
                '''Se transforma la acción seleccionada a una lista de acciones'''
                # la acción que se tomó corresponde a la del espacio de acciones que el agente tiene
                # asignado, pero según si es un agente convencional, competidor o propuesto, ese espacio
                # de acciones es diferente. Por esto, se implementa una desagregación de la acción en
                # las que controlan cada componente de la vivienda según corresponda.

                # El sistema propuesto controla todos los elementos del edificio, por lo que
                # se transforma la acción seleccionada del espacio de acciones a una lista que
                # asigna el control de cada uno de los elementos.  
                a_tp1_lista = EPsimulator.decimal_a_lista(a_tp1, 4)
                a_tp1_aa = a_tp1_lista[0]
                a_tp1_p = a_tp1_lista[1]
                a_tp1_vn = a_tp1_lista[2]
                a_tp1_vs = a_tp1_lista[3]
                

                '''Se ejecutan las acciones en el paso de tiempo actual'''
                # Aquí se está enviando información al simulador, asignando las acciones en cada uno
                # de los elementos accionables (en este caso se realiza a través de un calendario de
                # disponibilidad)
                api.exchange.set_actuator_value(state, HVACControlHandle, a_tp1_aa)
                api.exchange.set_actuator_value(state, ShadingControlHandle, a_tp1_p)
                api.exchange.set_actuator_value(state, VentN_ControlHandle, a_tp1_vn)
                api.exchange.set_actuator_value(state, VentS_ControlHandle, a_tp1_vs)
                

    """
    AQUI SE ESTABLECEN LOS METODOS QUE REALIZAN LA EJECUCIÓN DE ENERGYPLUS
    """

    def runEP():
        """
        Este método establece la configuración necesaria para ejecutar el simulador EnergyPlus de 
        forma local y asigna el momento en el que se hace el intercambio con la función de intercambio
        de información EP_exchange_function.
        """
        global EPconfig
        # se establece un estado en el simulador (indispensable)
        state = api.state_manager.new_state()
        # se hace un reset del estado en el simulador para borrar cualquier archivo que pueda haber 
        # quedado en la memoria despues de una ejecución previa (recomendado)
        api.state_manager.reset_state(state)
        # se establece el punto de llamado para el intercambio de información con el simulador
        api.runtime.callback_begin_zone_timestep_after_init_heat_balance(state, EPsimulator.EP_exchange_function)
        # se corre el simulador
        try:
            api.runtime.run_energyplus(state, ['-d', EPconfig['Folder_Output'], '-w', EPconfig['Weather_file'], EPconfig['epJSON_file']])
        except:
            api.runtime.run_energyplus(state, ['-d', EPconfig['Folder_Output'], '-w', EPconfig['Weather_file'], EPconfig['epJSON_file']])
        # se elimina el estado para evitar posibles errores en la memoria (opcional)(con la versión EP 960
        # esto arroja error)
        ExternalEnv.end_episode(ExternalEnv, EPconfig['episode'], EPconfig['last_observation'])


    def init_EPRandomConvergence():
        """
        """
        global first_episode, EPconfig

        EPconfig = {
            'episode_max': 5000,
            'episode':0,
            'beta': 20,
            'psi': 0.02,
            'rho': 2,
            'T_SP': 24,
            'dT_up': 1,
            'dT_dn': 1,
            'SP_RH': 70,
            'Folder_Output': "C:/Users/grhen/Documents/RLforEP_Resultados",
            'Weather_file': "C:/Users/grhen/Documents/GitHub/RLforEP/EP_Wheater_Configuration/Observatorio-hour_2.epw",
            'epJSON_file': "C:/Users/grhen/Documents/GitHub/RLforEP/EP_IDF_Configuration/modelo_simple_vent_mV950.epJSON",
            'last_observation': 0.
        }



        k = 0
        while k < EPconfig['episode_max']:
            EPconfig['episode'] = ExternalEnv.start_episode(
                ExternalEnv,
                episode_id = None,
                training_enabled = False
                )

            # Se seleccionan las condiciones iniciales
            month = int(np.random.randint(1, 13, 1))
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                day = int(np.random.randint(1, 32, 1))
            elif month == 2:
                day = int(np.random.randint(1, 29, 1))
            else:
                day = int(np.random.randint(1, 31, 1))
            
            # Se crea el archivo epJSON para el episodio
            EPconfig['epJSON_file'] = EPsimulator.episode_epJSON(month, day)
            
            EPsimulator.runEP()
            
            first_episode = False
            k += 1

    def init_customEnv():
        EPsimulator.init_EPRandomConvergence()
