"""
Entorno externo para RLlib que ejecuta EnergyPlus
"""
from six.moves import queue
import gym
import threading
import uuid
from typing import Optional

from ray.rllib.utils.annotations import PublicAPI
from ray.rllib.utils.typing import EnvActionType, EnvObsType, EnvInfoDict
import sys
sys.path.insert(0, 'C:/Users/grhen/Documents/GitHub/EP_RLlib')

import sys
sys.path.insert(0, 'C:/EnergyPlusV9-5-0')
from pyenergyplus.api import EnergyPlusAPI
api = EnergyPlusAPI()

from IDF_tool import Schedules, LocationClimate, MainFunctions
import numpy as np
import time
import os
import shutil
import pandas as pd

@PublicAPI
class EPExternalEnv(threading.Thread):
    """An environment that interfaces with external agents.

    Unlike simulator envs, control is inverted: The environment queries the
    policy to obtain actions and in return logs observations and rewards for
    training. This is in contrast to gym.Env, where the algorithm drives the
    simulation through env.step() calls.

    You can use ExternalEnv as the backend for policy serving (by serving HTTP
    requests in the run loop), for ingesting offline logs data (by reading
    offline transitions in the run loop), or other custom use cases not easily
    expressed through gym.Env.

    ExternalEnv supports both on-policy actions (through self.get_action()),
    and off-policy actions (through self.log_action()).

    This env is thread-safe, but individual episodes must be executed serially.

    Examples:
        >>> register_env("my_env", lambda config: YourExternalEnv(config))
        >>> trainer = DQNTrainer(env="my_env")
        >>> while True:
        >>>     print(trainer.train())
    """

    @PublicAPI
    def __init__(self,
                 action_space: gym.Space,
                 observation_space: gym.Space,
                 max_concurrent: int = 100,
                 config = {
                    'Folder_Output': '',
                    'Weather_file': '',
                    'epJSON_file': '',
                    'episode': 0,
                    'last_observation': [],
                    'T_SP': 24.,
                    'dT_up': 1.,
                    'dT_dn': 1.,
                    'SP_RH': 70.,
                    'rho': 0.25,
                    'beta': 20,
                    'psi': 0.005,
                    'first_time_step': True,
                    'directorio': '',
                    'ruta_base': 'C:/Users/grhen/Documents/GitHub/RLforEP',
                    'ruta': 'A' # A-Notebook Lenovo, B-Computadora grupo/Notebook Asus
                 }):
        """Initializes an ExternalEnv instance.

        Args:
            action_space: Action space of the env.
            observation_space: Observation space of the env.
            max_concurrent: Max number of active episodes to allow at
                once. Exceeding this limit raises an error.
        """

        threading.Thread.__init__(self)

        self.daemon = True
        self.action_space = action_space
        self.observation_space = observation_space
        self._episodes = {}
        self._finished = set()
        self._results_avail_condition = threading.Condition()
        self._max_concurrent_episodes = max_concurrent

        self.EnvConfig = config
        

        """
        Se establece la ruta base de los datos del programa
        """
        # Estas rutas deben coincidir con las del ordenador que se está utilizando
        if self.EnvConfig['ruta'] == "A":
            self.EnvConfig['ruta_base'] = 'C:/Users/grhen/Documents/GitHub/RLforEP'
            self.ruta_resultados = 'C:/Users/grhen/Documents/RLforEP_Resultados'

        elif self.EnvConfig['ruta'] == "B":
            self.EnvConfig['ruta_base'] = 'D:/GitHub/RLforEP/RLforEP_vent'
            self.ruta_resultados = 'D:/Resultados_RLforEP'
        else:
            self.EnvConfig['ruta_base'] = 'C:/Users/grhen/Documents/GitHub/RLforEP'
            self.ruta_resultados = 'C:/Users/grhen/Documents/RLforEP_Resultados'

        fecha = str(time.strftime('%y-%m-%d'))
        hora = str(time.strftime('%H-%M'))
        self.EnvConfig['directorio'] = self.EnvConfig['ruta_base'] + '/' + fecha + '-'+ hora
        try:
            os.mkdir(self.EnvConfig['directorio'])
            os.mkdir(self.EnvConfig['directorio']+'/Resultados')
        except OSError:
            time.sleep(60)
            os.mkdir(self.EnvConfig['directorio'])
            os.mkdir(self.EnvConfig['directorio']+'/Resultados')
            print("Se ha creado el directorio: %s " % self.EnvConfig['directorio'])
        except:
            print("La creación del directorio %s falló" % self.EnvConfig['directorio'])
        else:
            print("Se ha creado el directorio: %s " % self.EnvConfig['directorio'])

        shutil.copy(self.EnvConfig['ruta_base'] + '/experimento_parametros.json', self.EnvConfig['directorio'] + '/Resultados/experimento_parametros.json')
        
        # Para versión 950
        shutil.copy(self.EnvConfig['ruta_base'] + '/EP_IDF_Configuration/modelo_simple_vent_mV950_model2.epJSON', self.EnvConfig['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        # Para versión 960
        #shutil.copy(self.EnvConfig['ruta_base'] + '/EP_IDF_Configuration/modelo_simple_vent_m.epJSON', self.EnvConfig['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        
        shutil.copy(self.EnvConfig['ruta_base'] + '/EP_Wheater_Configuration/Observatorio-hour_2.epw', self.EnvConfig['directorio'] + '/Resultados/Observatorio-hour_2.epw')
 
        shutil.copy(self.EnvConfig['ruta_base'] + '/EP_IDF_Configuration/RL_Control_Sch_0.csv', self.EnvConfig['directorio'] + '/Resultados/RL_Control_Sch_0.csv')
        shutil.copy(self.EnvConfig['ruta_base'] + '/EP_IDF_Configuration/RL_Aviability_Sch_0.csv', self.EnvConfig['directorio'] + '/Resultados/RL_Aviability_Sch_0.csv')
        shutil.copy(self.EnvConfig['ruta_base'] + '/EP_IDF_Configuration/VentS_Aviability_Sch_0.csv', self.EnvConfig['directorio'] + '/Resultados/VentS_Aviability_Sch_0.csv')
        shutil.copy(self.EnvConfig['ruta_base'] + '/EP_IDF_Configuration/VentN_Aviability_Sch_0.csv', self.EnvConfig['directorio'] + '/Resultados/VentN_Aviability_Sch_0.csv')

        '''Se establece una etiqueta para identificar los parametros con los que se simulo el experimento'''
        output = [('simulacion_n', 'lr', 'gamma', 'qA', 'qS', 'Q_value', 'beta', 'rho', 'SP_temp', 'dT_up', 'dT_dn', 'n_episodios', 'power', 'eps', 'eps_decay', 'timestep_random', 'total_rew', 'total_ener', 'total_conf')]
        pd.DataFrame(output).to_csv(self.EnvConfig['directorio'] + '/Resultados/output_conv.csv', mode="w", index=False, header=False)
        pd.DataFrame(output).to_csv(self.EnvConfig['directorio'] + '/Resultados/output_comp.csv', mode="w", index=False, header=False)
        pd.DataFrame(output).to_csv(self.EnvConfig['directorio'] + '/Resultados/output_prop.csv', mode="w", index=False, header=False)
        
        
        #self.EnvConfig['directorio'] = EPExternalEnv.directorio(EPExternalEnv)

        self.EnvConfig['Folder_Output'] = self.EnvConfig['directorio']
        self.EnvConfig['Weather_file'] = self.EnvConfig['directorio'] + '/Resultados/Observatorio-hour_2.epw'
        self.EnvConfig['epJSON_file'] = self.EnvConfig['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON'


    @PublicAPI
    def run(self):
        """
        Este método establece la configuración necesaria para ejecutar el simulador EnergyPlus de 
        forma local y asigna el momento en el que se hace el intercambio con la función de intercambio
        de información EP_exchange_function.
        """

        self.EnvConfig['episode'] = self.start_episode(self)
        # se establece un estado en el simulador (indispensable)
        state = api.state_manager.new_state()
        # se hace un reset del estado en el simulador para borrar cualquier archivo que pueda haber 
        # quedado en la memoria despues de una ejecución previa (recomendado)
        api.state_manager.reset_state(state)
        # se establece el punto de llamado para el intercambio de información con el simulador
        api.runtime.callback_begin_zone_timestep_after_init_heat_balance(state, self.EP_exchange_function)
        # se corre el simulador
        try:
            api.runtime.run_energyplus(state, ['-d', self.EnvConfig['Folder_Output'], '-w', self.EnvConfig['Weather_file'], self.EnvConfig['epJSON_file']])
        except:
            api.runtime.run_energyplus(state, ['-d', self.EnvConfig['Folder_Output'], '-w', self.EnvConfig['Weather_file'], self.EnvConfig['epJSON_file']])
        # se elimina el estado para evitar posibles errores en la memoria (opcional)(con la versión EP 960
        # esto arroja error)
        self.end_episode(self.EnvConfig['episode'], self.EnvConfig['last_observation'])


    def decimal_a_lista(decimal, len):
        '''
        Esta función transforma una acción del espacio de acciones (entero) a una lista de longitud 
        asignada que contiene el valor binario del entero. 
        '''
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

    def episode_epJSON(self, month, day):
        """
        Este toma un archivo epJSON y lo modifica. Luego retorna la ruta del archivo modificado.
        Las modificaciones efectuadas son:
            1. Cambio del mes a ejecutar.
            2. Cambio del día a ejecutar.
            3. Cambio en los path de los calendarios de disponibilidad de los objetos accionables en la vivienda.
        """
        epJSON_file_old = MainFunctions.MainFunctions.read_epjson(self.EnvConfig['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        LocationClimate.RunPeriod.begin_day_of_month(epJSON_file_old, "DDMM", day)
        LocationClimate.RunPeriod.begin_month(epJSON_file_old, "DDMM", month)
        LocationClimate.RunPeriod.end_day_of_month(epJSON_file_old, "DDMM", day)
        LocationClimate.RunPeriod.end_month(epJSON_file_old, "DDMM", month)
        Schedules.Schedule_File.file_name(epJSON_file_old, "Aviability_Control", self.EnvConfig['directorio'] + '/Resultados/RL_Aviability_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "Shadow_Control", self.EnvConfig['directorio'] + '/Resultados/RL_Control_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "VentN_Control", self.EnvConfig['directorio'] + '/Resultados/VentN_Aviability_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "VentS_Control", self.EnvConfig['directorio'] + '/Resultados/VentS_Aviability_Sch_0.csv')
        MainFunctions.MainFunctions.write_epjson(self.EnvConfig['directorio'] + '/Resultados/new.epJSON', epJSON_file_old)
        epJSON_new = self.EnvConfig['directorio'] + '/Resultados/new.epJSON'

        return epJSON_new


    @PublicAPI
    def start_episode(self,
                      episode_id: Optional[str] = None,
                      training_enabled: bool = True) -> str:
        """
        Record the start of an episode.

        Args:
            episode_id: Unique string id for the episode or
                None for it to be auto-assigned and returned.
            training_enabled: Whether to use experiences for this
                episode to improve the policy.

        Returns:
            Unique string id for the episode.
        """

        if episode_id is None:
            episode_id = uuid.uuid4().hex

        if episode_id in self._finished:
            raise ValueError(
                "Episode {} has already completed.".format(episode_id))

        if episode_id in self._episodes:
            raise ValueError(
                "Episode {} is already started".format(episode_id))

        self._episodes[episode_id] = _ExternalEnvEpisode(
            episode_id, self._results_avail_condition, training_enabled)

        return episode_id

    @PublicAPI
    def get_action(self, episode_id: str,
                   observation: EnvObsType) -> EnvActionType:
        """
        Record an observation and get the on-policy action.

        Args:
            episode_id: Episode id returned from start_episode().
            observation: Current environment observation.

        Returns:
            Action from the env action space.
        """

        episode = self._get(episode_id)
        return episode.wait_for_action(observation)

    @PublicAPI
    def log_action(self, episode_id: str, observation: EnvObsType,
                   action: EnvActionType) -> None:
        """
        Record an observation and (off-policy) action taken.

        Args:
            episode_id: Episode id returned from start_episode().
            observation: Current environment observation.
            action: Action for the observation.
        """

        episode = self._get(episode_id)
        episode.log_action(observation, action)

    @PublicAPI
    def log_returns(self,
                    episode_id: str,
                    reward: float,
                    info: Optional[EnvInfoDict] = None) -> None:
        """
        Records returns (rewards and infos) from the environment.

        The reward will be attributed to the previous action taken by the
        episode. Rewards accumulate until the next action. If no reward is
        logged before the next action, a reward of 0.0 is assumed.

        Args:
            episode_id: Episode id returned from start_episode().
            reward: Reward from the environment.
            info: Optional info dict.
        """

        episode = self._get(episode_id)
        episode.cur_reward += reward

        if info:
            episode.cur_info = info or {}

    @PublicAPI
    def end_episode(self, episode_id: str, observation: EnvObsType) -> None:
        """
        Records the end of an episode.

        Args:
            episode_id: Episode id returned from start_episode().
            observation: Current environment observation.
        """

        episode = self._get(episode_id)
        self._finished.add(episode.episode_id)
        episode.done(observation)

    def _get(self, episode_id: str) -> "_ExternalEnvEpisode":
        """
        Get a started episode by its ID or raise an error."""

        if episode_id in self._finished:
            raise ValueError(
                "Episode {} has already completed.".format(episode_id))

        if episode_id not in self._episodes:
            raise ValueError("Episode {} not found.".format(episode_id))

        return self._episodes[episode_id]

    def EP_exchange_function(self, state):
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
                self.EnvConfig['last_observation'] = s_cont_tp1

                """
                CÁLCULO DE ENERGÍA, CONFORT Y RECOMPENSA
                """
                # handle for the energy consumption for cooling
                q_supp_handle = api.exchange.get_meter_handle(state, 'Cooling:DistrictCooling')
                q_supp = api.exchange.get_meter_value(state, q_supp_handle)

                # The energy consumption e is equal to the q_supp value but in kWh not in J
                e_tp1 = q_supp/(3.6*1000000)

                #La recompensa es calculada a partir de la energía y los minutos de confort
                if Ti > self.EnvConfig['T_SP'] + self.EnvConfig['dT_up'] or Ti < self.EnvConfig['T_SP'] - self.EnvConfig['dT_dn']:
                    if RHi > self.EnvConfig['SP_RH']:
                        r_temp = - self.EnvConfig['rho']*(Ti - self.EnvConfig['T_SP'])**2
                        r_hr = - self.EnvConfig['psi']*(RHi - self.EnvConfig['SP_RH'])**2
                    else:
                        r_temp = - self.EnvConfig['rho']*(Ti - self.EnvConfig['T_SP'])**2
                        r_hr = self.EnvConfig['psi'] * 10

                elif RHi > self.EnvConfig['SP_RH']:
                    r_temp = self.EnvConfig['rho'] * 10
                    r_hr = - self.EnvConfig['psi']*(RHi - self.EnvConfig['SP_RH'])**2

                else:
                    r_temp = self.EnvConfig['rho'] * 10
                    r_hr = self.EnvConfig['psi'] * 10
                
                if e_tp1 > 0:
                    r_energia = - self.EnvConfig['beta']*e_tp1
                else:
                    r_energia = self.EnvConfig['beta']
                
                r_tp1 = r_energia + r_temp + r_hr

                """
                SE GRABAN LAS VARIABLES PARA EL TIEMPO t
                """
                if self.EnvConfig['first_time_step'] == False:
                    self.log_returns(self.EnvConfig['episode'], r_tp1, {})


                if self.EnvConfig['first_time_step'] == True:
                    self.EnvConfig['first_time_step'] = False

                """Se obtiene la acción de RLlib"""
                print(self.observation_space.contains(s_cont_tp1))
                a_tp1 = self.get_action(self.EnvConfig['episode'], s_cont_tp1)
                
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
                a_tp1_lista = self.decimal_a_lista(a_tp1, 4)
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

class _ExternalEnvEpisode:
    """
    Tracked state for each active episode.
    """

    def __init__(self,
                 episode_id: str,
                 results_avail_condition: threading.Condition,
                 training_enabled: bool,
                 multiagent: bool = False):
        self.episode_id = episode_id
        self.results_avail_condition = results_avail_condition
        self.training_enabled = training_enabled
        self.multiagent = multiagent
        self.data_queue = queue.Queue()
        self.action_queue = queue.Queue()
        if multiagent:
            self.new_observation_dict = None
            self.new_action_dict = None
            self.cur_reward_dict = {}
            self.cur_done_dict = {"__all__": False}
            self.cur_info_dict = {}
        else:
            self.new_observation = None
            self.new_action = None
            self.cur_reward = 0.0
            self.cur_done = False
            self.cur_info = {}

    def get_data(self):
        if self.data_queue.empty():
            return None
        return self.data_queue.get_nowait()

    def log_action(self, observation, action):
        if self.multiagent:
            self.new_observation_dict = observation
            self.new_action_dict = action
        else:
            self.new_observation = observation
            self.new_action = action
        self._send()
        self.action_queue.get(True, timeout=60.0)

    def wait_for_action(self, observation):
        if self.multiagent:
            self.new_observation_dict = observation
        else:
            self.new_observation = observation
        self._send()
        return self.action_queue.get(True, timeout=300.0)

    def done(self, observation):
        if self.multiagent:
            self.new_observation_dict = observation
            self.cur_done_dict = {"__all__": True}
        else:
            self.new_observation = observation
            self.cur_done = True
        self._send()

    def _send(self):
        if self.multiagent:
            if not self.training_enabled:
                for agent_id in self.cur_info_dict:
                    self.cur_info_dict[agent_id]["training_enabled"] = False
            item = {
                "obs": self.new_observation_dict,
                "reward": self.cur_reward_dict,
                "done": self.cur_done_dict,
                "info": self.cur_info_dict,
            }
            if self.new_action_dict is not None:
                item["off_policy_action"] = self.new_action_dict
            self.new_observation_dict = None
            self.new_action_dict = None
            self.cur_reward_dict = {}
        else:
            item = {
                "obs": self.new_observation,
                "reward": self.cur_reward,
                "done": self.cur_done,
                "info": self.cur_info,
            }
            if self.new_action is not None:
                item["off_policy_action"] = self.new_action
            self.new_observation = None
            self.new_action = None
            self.cur_reward = 0.0
            if not self.training_enabled:
                item["info"]["training_enabled"] = False

        with self.results_avail_condition:
            self.data_queue.put_nowait(item)
            self.results_avail_condition.notify()


if "__main__" == __name__:
    EPExternalEnv.run()