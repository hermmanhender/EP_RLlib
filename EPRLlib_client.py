#!/usr/bin/env python
"""
# EPRLlib_client (ExternalEnv)

Running an external simulator against an RLlib policy server listening on one or more
HTTP-speaking port(s). See `EPRLlib_server.py` in this same directory for
how to start this server.

Setup:
1) Start the policy server:
    See `EPRLlib_server.py` on how to do this.
2) Run this client:
    $ python EPRLlib_client.py --inference-mode=local|remote --[other options]
      Use --help for help.

In "local" inference-mode, the action computations are performed
inside the PolicyClient used in this script w/o sending an HTTP request
to the server. This reduces network communication overhead, but requires
the PolicyClient to create its own RolloutWorker (+Policy) based on
the server's config. The PolicyClient will retrieve this config automatically.
You do not need to define the RLlib config dict here!

In "remote" inference mode, the PolicyClient will send action requests to the
server and not compute its own actions locally. The server then performs the
inference forward pass and returns the action to the client.

In either case, the user of PolicyClient must:
- Declare new episodes and finished episodes to the PolicyClient.
- Log rewards to the PolicyClient.
- Call `get_action` to receive an action from the PolicyClient (whether it'd be
  computed locally or remotely).
- Besides `get_action`, the user may let the PolicyClient know about
  off-policy actions having been taken via `log_action`. This can be used in
  combination with `get_action`, but will only work, if the connected server
  runs an off-policy RL algorithm (such as DQN, SAC, or DDPG).
"""


from email.policy import Policy
import sys
sys.path.insert(0, 'C:/Users/grhen/Documents/GitHub/EP_RLlib')
sys.path.insert(0, 'C:/EnergyPlusV22-1-0')
from pyenergyplus.api import EnergyPlusAPI
api = EnergyPlusAPI()

from IDF_tool import Schedules, LocationClimate, MainFunctions
import time
import os
import shutil
import pandas as pd
import argparse
import numpy as np

from ray.rllib.utils.annotations import PublicAPI

from ray.rllib.env.policy_client import PolicyClient

@PublicAPI
class environment():

    global client, config

    @PublicAPI
    def __init__(self):
        """
        Se establece la ruta base de los datos del programa
        """
        RAY_DISABLE_MEMORY_MONITOR = 1
        # Estas rutas deben coincidir con las del ordenador que se está utilizando
        if config['ruta'] == "A":
            config['ruta_base'] = 'C:/Users/grhen/Documents/GitHub/EP_RLlib'
            self.ruta_resultados = 'C:/Users/grhen/Documents/RLforEP_Resultados'

        elif config['ruta'] == "B":
            config['ruta_base'] = 'D:/GitHub/EP_RLlib'
            self.ruta_resultados = 'D:/Resultados_RLforEP'
        elif config['ruta'] == "C":
            config['ruta_base'] = 'D:/GitHub/EP_RLlib'
            self.ruta_resultados = 'D:/Resultados_RLforEP'
        else:
            config['ruta_base'] = 'C:/Users/grhen/Documents/GitHub/EP_RLlib'
            self.ruta_resultados = 'C:/Users/grhen/Documents/RLforEP_Resultados'

        fecha = str(time.strftime('%y-%m-%d'))
        hora = str(time.strftime('%H-%M'))
        caso = config['nombre_caso']
        config['directorio'] = self.ruta_resultados + '/' + fecha + '-'+ hora + '_'+ caso
        try:
            os.mkdir(config['directorio'])
            os.mkdir(config['directorio']+'/Resultados')
        except OSError:
            time.sleep(60)
            os.mkdir(config['directorio'])
            os.mkdir(config['directorio']+'/Resultados')
            print("Se ha creado el directorio: %s " % config['directorio'])
        except:
            print("La creación del directorio %s falló" % config['directorio'])
        else:
            print("Se ha creado el directorio: %s " % config['directorio'])

        #shutil.copy(config['ruta_base'] + '/experimento_parametros.json', config['directorio'] + '/Resultados/experimento_parametros.json')
        
        # Para versión 950
        #shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/modelo_simple_vent_mV950_model2.epJSON', config['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        # Para versión 960
        #shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/modelo_simple_vent_m.epJSON', config['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        # Para versión 2210
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/modelo_simple_V2210.epJSON', config['directorio'] + '/Resultados/modelo_simple.epJSON')
        shutil.copy(config['ruta_base'] + '/EP_Wheater_Configuration/Observatorio-hour_2.epw', config['directorio'] + '/Resultados/Observatorio-hour_2.epw')

        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/RL_Control_Sch_0.csv', config['directorio'] + '/Resultados/RL_Control_Sch_0.csv')
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/RL_Aviability_Sch_C_0.csv', config['directorio'] + '/Resultados/RL_Aviability_Sch_C_0.csv')
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/RL_Aviability_Sch_R_0.csv', config['directorio'] + '/Resultados/RL_Aviability_Sch_R_0.csv')
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/VentS_Aviability_Sch_0.csv', config['directorio'] + '/Resultados/VentS_Aviability_Sch_0.csv')
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/VentN_Aviability_Sch_0.csv', config['directorio'] + '/Resultados/VentN_Aviability_Sch_0.csv')

        '''Se establece una etiqueta para identificar los parametros con los que se simulo el experimento'''
        #output = [('simulacion_n', 'lr', 'gamma', 'qA', 'qS', 'Q_value', 'beta', 'rho', 'SP_temp', 'dT_up', 'dT_dn', 'n_episodios', 'power', 'eps', 'eps_decay', 'timestep_random', 'total_rew', 'total_ener', 'total_conf')]
        output = [('rad', 'Bw', 'To', 'Ti', 'v', 'd', 'RHi', 'a', 'a_tp1_R', 'a_tp1_C', 'a_tp1_p', 'a_tp1_vn', 'a_tp1_vs', 'total_rew', 'total_ener', 'total_conf')]
        #pd.DataFrame(output).to_csv(config['directorio'] + '/Resultados/output_conv.csv', mode="w", index=False, header=False)
        #pd.DataFrame(output).to_csv(config['directorio'] + '/Resultados/output_comp.csv', mode="w", index=False, header=False)
        pd.DataFrame(output).to_csv(config['directorio'] + '/Resultados/output_prop.csv', mode="w", index=False, header=False)
          
        #config['directorio'] = EPExternalEnv.directorio(EPExternalEnv)

        config['Folder_Output'] = config['directorio']
        config['Weather_file'] = config['directorio'] + '/Resultados/Observatorio-hour_2.epw'
        config['epJSON_file'] = config['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON'

    @PublicAPI
    def run(self):
        """
        Este método establece la configuración necesaria para ejecutar el simulador EnergyPlus de 
        forma local y asigna el momento en el que se hace el intercambio con la función de intercambio
        de información EP_exchange_function.
        """
        # se establece un estado en el simulador (indispensable)
        state = api.state_manager.new_state()
        # se hace un reset del estado en el simulador para borrar cualquier archivo que pueda haber 
        # quedado en la memoria despues de una ejecución previa (recomendado)
        api.state_manager.reset_state(state)
        # se establece el punto de llamado para el intercambio de información con el simulador
        api.runtime.callback_begin_zone_timestep_after_init_heat_balance(state, self.EP_exchange_function)
        # Se establece un dia random como periodo de duracion del episodio
        #month, day = self.random_run_date(self)
        # Si se quiere definir un periodo determinado, utilizar la siguiente parte del codigo
        month = 1
        day = 1
        #final_month = 3
        #final_day = 31
        config['epJSON_file'] = self.episode_epJSON(self, month, day) #, final_month, final_day)
        # se corre el simulador
        try:
            api.runtime.run_energyplus(state, ['-d', config['Folder_Output'], '-w', config['Weather_file'], config['epJSON_file']])
        except:
            api.runtime.run_energyplus(state, ['-d', config['Folder_Output'], '-w', config['Weather_file'], config['epJSON_file']])
        # se elimina el estado para evitar posibles errores en la memoria (opcional)(con la versión EP 960
        # esto arroja error)
        

    @PublicAPI
    def random_run_date(self):
        month = int(np.random.randint(1, 13, 1))
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day = int(np.random.randint(1, 32, 1))
        elif month == 2:
            day = int(np.random.randint(1, 29, 1))
        else:
            day = int(np.random.randint(1, 31, 1))

        return month, day

    @PublicAPI
    def episode_epJSON(self, init_month, init_day, final_month=0, final_day=0):
        """
        Este toma un archivo epJSON y lo modifica. Luego retorna la ruta del archivo modificado.
        Las modificaciones efectuadas son:
            1. Cambio del mes a ejecutar.
            2. Cambio del día a ejecutar.
            3. Cambio en los path de los calendarios de disponibilidad de los objetos accionables en la vivienda.
        """
        if final_month == 0:
            final_month = init_month
        if final_day == 0:
            final_day = init_day
        
        epJSON_file_old = MainFunctions.MainFunctions.read_epjson(config['directorio'] + '/Resultados/modelo_simple.epJSON')
        LocationClimate.RunPeriod.begin_day_of_month(epJSON_file_old, "DDMM", init_day)
        LocationClimate.RunPeriod.begin_month(epJSON_file_old, "DDMM", init_month)
        LocationClimate.RunPeriod.end_day_of_month(epJSON_file_old, "DDMM", final_day)
        LocationClimate.RunPeriod.end_month(epJSON_file_old, "DDMM", final_month)
        Schedules.Schedule_File.file_name(epJSON_file_old, "Aviability_Control_R", config['directorio'] + '/Resultados/RL_Aviability_Sch_R_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "Aviability_Control_C", config['directorio'] + '/Resultados/RL_Aviability_Sch_C_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "Shadow_Control", config['directorio'] + '/Resultados/RL_Control_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "VentN_Control", config['directorio'] + '/Resultados/VentN_Aviability_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "VentS_Control", config['directorio'] + '/Resultados/VentS_Aviability_Sch_0.csv')
        MainFunctions.MainFunctions.write_epjson(config['directorio'] + '/Resultados/new.epJSON', epJSON_file_old)
        epJSON_new = config['directorio'] + '/Resultados/new.epJSON'

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

                # Se inicia el episodio en el servidor
                if time_step + (hour * num_time_steps_in_hour) == 1:
                    config['episode'] = client.start_episode()

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
                s_cont_tp1 = [rad, Bw, To, Ti, v, d, RHi]
                config['last_observation'] = s_cont_tp1

                """
                CÁLCULO DE ENERGÍA, CONFORT Y RECOMPENSA
                """
                # handle for the energy consumption for cooling
                q_R_handle = api.exchange.get_meter_handle(state, 'Cooling:DistrictCooling')
                q_R = api.exchange.get_meter_value(state, q_R_handle)

                q_C_handle = api.exchange.get_meter_handle(state, 'Heating:DistrictHeating')
                q_C = api.exchange.get_meter_value(state, q_C_handle)

                # The energy consumption e is equal to the q_supp value but in kWh not in J
                e_tp1 = (q_R + q_C)/(3.6*1000000)

                # Handle for Fanger PPD (range 0 - 100)
                # This field is the “predicted percentage of dissatisfied” (PPD) calculated using the Fanger thermal
                # comfort model. Details on the equations used to calculate the Fanger PPD are shown in the EnergyPlus
                # Engineering Reference. If the zone in question is currently being controlled using a thermostat object,
                # then the value of the PPD is determined by using the air temperature and humidity that is calculated
                # at the system time step; otherwise, if the zone is uncontrolled, the PPD is determined using the zone air
                # temperature and humidity that is averaged over the zone time step.
                PPD_handle = api.exchange.get_variable_handle(state, "Zone Thermal Comfort Fanger Model PPD", "Thermal Zone: Modelo_Simple")
                
                # Handle for Fanger PMV (range (-4) - 4)
                # This field is the “predicted mean vote” (PMV) calculated using the Fanger thermal comfort model.
                # Details on the equations used to calculate the Fanger PMV are shown in the EnergyPlus Engineering
                # Reference. If the zone in question is currently being controlled using a thermostat object, then the value
                # of the PMV is determined by using the air temperature and humidity that is calculated at the system time
                # step; otherwise, if the zone is uncontrolled, the PMV is determined using the zone air temperature and
                # humidity that is averaged over the zone time step.
                PMV_handle = api.exchange.get_variable_handle(state, "Zone Thermal Comfort Fanger Model PMV", "Thermal Zone: Modelo_Simple")

                # PMV value
                c_tp1 = api.exchange.get_variable_value(state, PMV_handle)
                print("PMV: " + str(c_tp1))

                # PPD value
                PPD_v = api.exchange.get_variable_value(state, PPD_handle)
                print("PPD: " + str(PPD_v))
                
                """
                # Minutes comfort calculation
                if Ti > (config["T_SP"] + config['dT_up']) or Ti < (config["T_SP"] - config['dT_dn']): # or RHi > config['SP_RH']:
                    c_tp1 = 0
                elif Ti <= (config["T_SP"] + config['dT_up']) or Ti >= (config["T_SP"] - config['dT_dn']): # or RHi <= config['SP_RH']:
                    c_tp1 = 60/num_time_steps_in_hour
                else:
                    print("Comfort not founded.")
                    c_tp1 = -1
                """

                # La recompensa es calculada a partir de la energía y los minutos de confort
                r_tp1 = - e_tp1 - config['rho']*(c_tp1**2)

                """
                # Se evalúa el confort higro-térmico
                if Ti > config['T_SP'] + config['dT_up'] or Ti < config['T_SP'] - config['dT_dn']:
                    if RHi > config['SP_RH']:
                        r_temp = - config['rho']*(Ti - config['T_SP'])**2 # penalización por temperatura
                        r_hr = - config['psi']*(RHi - config['SP_RH'])**2 # penalización por humedad
                    else:
                        r_temp = - config['rho']*(Ti - config['T_SP'])**2 # penalización por temperatura
                        r_hr = config['psi'] * 10 # recompensa por humedad

                elif RHi > config['SP_RH']:
                    r_temp = config['rho'] * 100 # recompensa por temperatura
                    r_hr = - config['psi']*(RHi - config['SP_RH'])**2 # penalización por humedad

                else:
                    r_temp = config['rho'] * 100 # recompensa por temperatura
                    r_hr = config['psi'] * 10 # recompensa por humedad
                # Se evalúa el uso de energía
                if e_tp1 > 0:
                    r_energia = - config['beta']*e_tp1 # penalización por energía
                else:
                    r_energia = config['beta'] # recompensa por energía
                
                r_tp1 = r_energia + r_temp + r_hr
                """

                if config['first_time_step'] == False:
                    client.log_returns(config['episode'], r_tp1, {})


                if config['first_time_step'] == True:
                    config['first_time_step'] = False

                """Se obtiene la acción de RLlib"""
                a_tp1 = client.get_action(config['episode'], s_cont_tp1)
                
                """
                SE REALIZAN LAS ACCIONES EN EL SIMULADOR
                """
                '''Se solicitan los handles de cada una de las variables que se quiere controlar'''
                # handle para el control de la persiana
                ShadingControlHandle = api.exchange.get_actuator_handle(state, 'Schedule:File', 'Schedule Value', 'Shadow_Control')
                # handle para el control del refrigerador
                R_ControlHandle = api.exchange.get_actuator_handle(state, 'Schedule:File', 'Schedule Value', 'Aviability_Control_R')
                # handle para el control del calefactor
                C_ControlHandle = api.exchange.get_actuator_handle(state, 'Schedule:File', 'Schedule Value', 'Aviability_Control_C')
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
                '''
                Esta función transforma una acción del espacio de acciones (entero) a una lista de longitud 
                asignada que contiene el valor binario del entero. 
                '''
                len = 5
                binario = []
                # se comprueba que el entero se pueda representar como un binario de la longitud asignada
                if a_tp1 >= 2**len:
                    print("Error: decimal out of range.")
                # se comprueba que el entero sea positivo
                elif a_tp1 < 0:
                    print("Error: decimal out of range.")
                # si el entero es 0, entonces el binario es una lista de la longitud especificada llena de ceros.
                elif a_tp1 == 0: 
                    i=0
                    while i <= len-1:
                        binario.append(0)
                        i+=1
                else:
                    i=0
                    while i <= len-1: # mientras el número de entrada sea diferente de cero
                        # paso 1: dividimos entre 2
                        modulo = a_tp1 % 2
                        cociente = a_tp1 // 2
                        binario.insert(0, modulo) # guardamos el módulo calculado
                        a_tp1 = cociente # el cociente pasa a ser el número de entrada
                        i += 1


                a_tp1_lista = binario

                a_tp1_R = a_tp1_lista[0]
                a_tp1_C = a_tp1_lista[1]
                a_tp1_p = a_tp1_lista[2]
                a_tp1_vn = a_tp1_lista[3]
                a_tp1_vs = a_tp1_lista[4]

                """
                SE GRABAN LAS VARIABLES PARA EL TIEMPO t
                """
                output = [(rad, Bw, To, Ti, v, d, RHi, a_tp1, a_tp1_R, a_tp1_C, a_tp1_p, a_tp1_vn, a_tp1_vs, r_tp1, e_tp1, c_tp1)]
                pd.DataFrame(output).to_csv(config['directorio'] + '/Resultados/output_prop.csv', mode="a", index=False, header=False)
                                

                '''Se ejecutan las acciones en el paso de tiempo actual'''
                # Aquí se está enviando información al simulador, asignando las acciones en cada uno
                # de los elementos accionables (en este caso se realiza a través de un calendario de
                # disponibilidad)
                api.exchange.set_actuator_value(state, R_ControlHandle, a_tp1_R)
                api.exchange.set_actuator_value(state, C_ControlHandle, a_tp1_C)
                api.exchange.set_actuator_value(state, ShadingControlHandle, a_tp1_p)
                api.exchange.set_actuator_value(state, VentN_ControlHandle, a_tp1_vn)
                api.exchange.set_actuator_value(state, VentS_ControlHandle, a_tp1_vs)

                if time_step + (hour * num_time_steps_in_hour) >= num_time_steps_in_hour*24:
                    client.end_episode(config['episode'], config['last_observation'])
                    output = [("episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end", "episode_end")]
                    pd.DataFrame(output).to_csv(config['directorio'] + '/Resultados/output_prop.csv', mode="a", index=False, header=False)
                



parser = argparse.ArgumentParser()
parser.add_argument(
    "--no-train",
    action="store_true",
    help="Whether to disable training."
)
parser.add_argument(
    "--inference-mode",
    type=str,
    default="local",
    choices=["local", "remote"]
)
parser.add_argument(
    "--off-policy",
    action="store_true",
    help="Whether to compute random actions instead of on-policy "
    "(Policy-computed) ones.",
)
parser.add_argument(
    "--stop-reward",
    type=float,
    default=9999,
    help="Stop once the specified reward is reached.",
)
parser.add_argument(
    "--port",
    type=int,
    default=9900,
    help="The port to use (on localhost)."
)

config = {'Folder_Output': '',
        'Weather_file': '',
        'epJSON_file': '',
        'episode': 0,
        'last_observation': [],
        'T_SP': 24.,
        'dT_up': 1.,
        'dT_dn': 4.,
        'SP_RH': 70.,
        'nombre_caso': "rho10-100", # Se utiliza para identificar la carpeta donde se guardan los datos
        'rho': 10, # Temperatura: default: 0.25
        'beta': 1, # Energía: default: 20
        'psi': 0, # Humedad relativa: default: 0.005
        'first_time_step': True,
        'directorio': '',
        'ruta_base': 'C:/Users/grhen/Documents/GitHub/RLforEP',
        'ruta': 'A' # A-Notebook Lenovo, B-Notebook Asus, C-Computadora grupo
        }

if __name__ == "__main__":
    args = parser.parse_args()

    client = PolicyClient(
        f"http://localhost:{args.port}", inference_mode=args.inference_mode
        )
    
    environment()

    n = 0
    while n < 1000:
        print("\nEpisode "+ str(n+1))
        environment.run(environment)
        n += 1
        if n % 100 == 0:
            print("Se obtienen los pesos de la DQN.")
            weights = client.GET_WEIGHTS()
            pd.DataFrame(weights).to_csv(config['directorio'] + '/Resultados/weights_prop.csv', mode="a", index=False, header=False)
            
    print("Se obtienen los pesos finales de la DQN.")
    weights = client.GET_WEIGHTS()
    pd.DataFrame(weights).to_csv(config['directorio'] + '/Resultados/weights_prop.csv', mode="a", index=False, header=False)