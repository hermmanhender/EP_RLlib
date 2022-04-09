from six.moves import queue
import gym
from gym import spaces
import threading
import uuid
from typing import Callable, Tuple, Optional, TYPE_CHECKING

from ray.rllib.env.base_env import BaseEnv
from ray.rllib.utils.annotations import override, PublicAPI
from ray.rllib.utils.typing import (
    EnvActionType,
    EnvInfoDict,
    EnvObsType,
    EnvType,
    MultiEnvDict,
)

if TYPE_CHECKING:
    from ray.rllib.models.preprocessors import Preprocessor

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
import numpy as np


@PublicAPI
class ExternalEnv(threading.Thread):
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
        >>> from ray.tune import register_env
        >>> from ray.rllib.agents.dqn import DQNTrainer # doctest: +SKIP
        >>> YourExternalEnv = ... # doctest: +SKIP
        >>> register_env("my_env", # doctest: +SKIP
        ...     lambda config: YourExternalEnv(config))
        >>> trainer = DQNTrainer(env="my_env") # doctest: +SKIP
        >>> while True: # doctest: +SKIP
        >>>     print(trainer.train()) # doctest: +SKIP
    """
    
    global config

    @PublicAPI
    def __init__(
        self,
        action_space: spaces.Discrete(16),
        observation_space: spaces.Box(float("-inf"), float("inf"), (7,)),
        max_concurrent: int = 100,
    ):
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

        """
        Se establece la ruta base de los datos del programa
        """
        # Estas rutas deben coincidir con las del ordenador que se está utilizando
        if config['ruta'] == "A":
            config['ruta_base'] = 'C:/Users/grhen/Documents/GitHub/RLforEP'
            self.ruta_resultados = 'C:/Users/grhen/Documents/RLforEP_Resultados'

        elif config['ruta'] == "B":
            config['ruta_base'] = 'D:/GitHub/RLforEP/RLforEP_vent'
            self.ruta_resultados = 'D:/Resultados_RLforEP'
        elif config['ruta'] == "C":
            config['ruta_base'] = 'D:/GitHub/RLforEP/RLforEP'
            self.ruta_resultados = 'D:/Resultados_RLforEP'
        else:
            config['ruta_base'] = 'C:/Users/grhen/Documents/GitHub/RLforEP'
            self.ruta_resultados = 'C:/Users/grhen/Documents/RLforEP_Resultados'

        fecha = str(time.strftime('%y-%m-%d'))
        hora = str(time.strftime('%H-%M'))
        config['directorio'] = self.ruta_resultados + '/' + fecha + '-'+ hora
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

        shutil.copy(config['ruta_base'] + '/experimento_parametros.json', config['directorio'] + '/Resultados/experimento_parametros.json')
        
        # Para versión 950
        #shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/modelo_simple_vent_mV950_model2.epJSON', config['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        # Para versión 960
        #shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/modelo_simple_vent_m.epJSON', config['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        # Para versión 2210
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/modelo_simple_vent_m_V2210.epJSON', config['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        shutil.copy(config['ruta_base'] + '/EP_Wheater_Configuration/Observatorio-hour_2.epw', config['directorio'] + '/Resultados/Observatorio-hour_2.epw')

        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/RL_Control_Sch_0.csv', config['directorio'] + '/Resultados/RL_Control_Sch_0.csv')
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/RL_Aviability_Sch_0.csv', config['directorio'] + '/Resultados/RL_Aviability_Sch_0.csv')
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/VentS_Aviability_Sch_0.csv', config['directorio'] + '/Resultados/VentS_Aviability_Sch_0.csv')
        shutil.copy(config['ruta_base'] + '/EP_IDF_Configuration/VentN_Aviability_Sch_0.csv', config['directorio'] + '/Resultados/VentN_Aviability_Sch_0.csv')

        '''Se establece una etiqueta para identificar los parametros con los que se simulo el experimento'''
        #output = [('simulacion_n', 'lr', 'gamma', 'qA', 'qS', 'Q_value', 'beta', 'rho', 'SP_temp', 'dT_up', 'dT_dn', 'n_episodios', 'power', 'eps', 'eps_decay', 'timestep_random', 'total_rew', 'total_ener', 'total_conf')]
        output = [('total_rew', 'total_ener', 'total_conf')]
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
        api.runtime.callback_begin_zone_timestep_after_init_heat_balance(state, self.EP_exchange_function(state))
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
        
        epJSON_file_old = MainFunctions.MainFunctions.read_epjson(config['directorio'] + '/Resultados/modelo_simple_vent_m.epJSON')
        LocationClimate.RunPeriod.begin_day_of_month(epJSON_file_old, "DDMM", init_day)
        LocationClimate.RunPeriod.begin_month(epJSON_file_old, "DDMM", init_month)
        LocationClimate.RunPeriod.end_day_of_month(epJSON_file_old, "DDMM", final_day)
        LocationClimate.RunPeriod.end_month(epJSON_file_old, "DDMM", final_month)
        Schedules.Schedule_File.file_name(epJSON_file_old, "Aviability_Control", config['directorio'] + '/Resultados/RL_Aviability_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "Shadow_Control", config['directorio'] + '/Resultados/RL_Control_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "VentN_Control", config['directorio'] + '/Resultados/VentN_Aviability_Sch_0.csv')
        Schedules.Schedule_File.file_name(epJSON_file_old, "VentS_Control", config['directorio'] + '/Resultados/VentS_Aviability_Sch_0.csv')
        MainFunctions.MainFunctions.write_epjson(config['directorio'] + '/Resultados/new.epJSON', epJSON_file_old)
        epJSON_new = config['directorio'] + '/Resultados/new.epJSON'

        return epJSON_new

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

                # Se inicia el episodio en el servidor
                if time_step + (hour * num_time_steps_in_hour) == 1:
                    config['episode'] = self.start_episode()

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
                q_supp_handle = api.exchange.get_meter_handle(state, 'Cooling:DistrictCooling')
                q_supp = api.exchange.get_meter_value(state, q_supp_handle)

                # The energy consumption e is equal to the q_supp value but in kWh not in J
                e_tp1 = q_supp/(3.6*1000000)

                # Minutes comfort calculation
                if Ti > (config["T_SP"] + config['dT_up']) or Ti < (config["T_SP"] - config['dT_dn']) or RHi > config['SP_RH']:
                    c_tp1 = 0
                elif Ti <= (config["T_SP"] + config['dT_up']) or Ti >= (config["T_SP"] - config['dT_dn']) or RHi <= config['SP_RH']:
                    c_tp1 = 60/num_time_steps_in_hour
                else:
                    print("Comfort not founded.")
                    c_tp1 = -1
                
                # La recompensa es calculada a partir de la energía y los minutos de confort
                if Ti > config['T_SP'] + config['dT_up'] or Ti < config['T_SP'] - config['dT_dn']:
                    if RHi > config['SP_RH']:
                        r_temp = - config['rho']*(Ti - config['T_SP'])**2
                        r_hr = - config['psi']*(RHi - config['SP_RH'])**2
                    else:
                        r_temp = - config['rho']*(Ti - config['T_SP'])**2
                        r_hr = config['psi'] * 10

                elif RHi > config['SP_RH']:
                    r_temp = config['rho'] * 10
                    r_hr = - config['psi']*(RHi - config['SP_RH'])**2

                else:
                    r_temp = config['rho'] * 10
                    r_hr = config['psi'] * 10
                
                if e_tp1 > 0:
                    r_energia = - config['beta']*e_tp1
                else:
                    r_energia = config['beta']
                
                r_tp1 = r_energia + r_temp + r_hr

                """
                SE GRABAN LAS VARIABLES PARA EL TIEMPO t
                """
                output = [(r_tp1, e_tp1, c_tp1)]
                pd.DataFrame(output).to_csv(config['directorio'] + '/Resultados/output_prop.csv', mode="a", index=False, header=False)
                
                if config['first_time_step'] == False:
                    self.log_returns(config['episode'], r_tp1, {})


                if config['first_time_step'] == True:
                    config['first_time_step'] = False

                """Se obtiene la acción de RLlib"""
                a_tp1 = self.get_action(config['episode'], s_cont_tp1)
                
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
                '''
                Esta función transforma una acción del espacio de acciones (entero) a una lista de longitud 
                asignada que contiene el valor binario del entero. 
                '''
                len = 4
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

                if time_step + (hour * num_time_steps_in_hour) >= num_time_steps_in_hour*24:
                    self.end_episode(config['episode'], config['last_observation'])
                    output = [("episode_end", "episode_end", "episode_end")]
                    pd.DataFrame(output).to_csv(config['directorio'] + '/Resultados/output_prop.csv', mode="a", index=False, header=False)
                

    @PublicAPI
    def start_episode(
        self, episode_id: Optional[str] = None, training_enabled: bool = True
    ) -> str:
        """Record the start of an episode.

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
            raise ValueError("Episode {} has already completed.".format(episode_id))

        if episode_id in self._episodes:
            raise ValueError("Episode {} is already started".format(episode_id))

        self._episodes[episode_id] = _ExternalEnvEpisode(
            episode_id, self._results_avail_condition, training_enabled
        )

        return episode_id

    @PublicAPI
    def get_action(self, episode_id: str, observation: EnvObsType) -> EnvActionType:
        """Record an observation and get the on-policy action.

        Args:
            episode_id: Episode id returned from start_episode().
            observation: Current environment observation.

        Returns:
            Action from the env action space.
        """

        episode = self._get(episode_id)
        return episode.wait_for_action(observation)

    @PublicAPI
    def log_action(
        self, episode_id: str, observation: EnvObsType, action: EnvActionType
    ) -> None:
        """Record an observation and (off-policy) action taken.

        Args:
            episode_id: Episode id returned from start_episode().
            observation: Current environment observation.
            action: Action for the observation.
        """

        episode = self._get(episode_id)
        episode.log_action(observation, action)

    @PublicAPI
    def log_returns(
        self, episode_id: str, reward: float, info: Optional[EnvInfoDict] = None
    ) -> None:
        """Records returns (rewards and infos) from the environment.

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
        """Records the end of an episode.

        Args:
            episode_id: Episode id returned from start_episode().
            observation: Current environment observation.
        """

        episode = self._get(episode_id)
        self._finished.add(episode.episode_id)
        episode.done(observation)

    def _get(self, episode_id: str) -> "_ExternalEnvEpisode":
        """Get a started episode by its ID or raise an error."""

        if episode_id in self._finished:
            raise ValueError("Episode {} has already completed.".format(episode_id))

        if episode_id not in self._episodes:
            raise ValueError("Episode {} not found.".format(episode_id))

        return self._episodes[episode_id]

    def to_base_env(
        self,
        make_env: Optional[Callable[[int], EnvType]] = None,
        num_envs: int = 1,
        remote_envs: bool = False,
        remote_env_batch_wait_ms: int = 0,
    ) -> "BaseEnv":
        """Converts an RLlib MultiAgentEnv into a BaseEnv object.

        The resulting BaseEnv is always vectorized (contains n
        sub-environments) to support batched forward passes, where n may
        also be 1. BaseEnv also supports async execution via the `poll` and
        `send_actions` methods and thus supports external simulators.

        Args:
            make_env: A callable taking an int as input (which indicates
                the number of individual sub-environments within the final
                vectorized BaseEnv) and returning one individual
                sub-environment.
            num_envs: The number of sub-environments to create in the
                resulting (vectorized) BaseEnv. The already existing `env`
                will be one of the `num_envs`.
            remote_envs: Whether each sub-env should be a @ray.remote
                actor. You can set this behavior in your config via the
                `remote_worker_envs=True` option.
            remote_env_batch_wait_ms: The wait time (in ms) to poll remote
                sub-environments for, if applicable. Only used if
                `remote_envs` is True.

        Returns:
            The resulting BaseEnv object.
        """
        if num_envs != 1:
            raise ValueError(
                "External(MultiAgent)Env does not currently support "
                "num_envs > 1. One way of solving this would be to "
                "treat your Env as a MultiAgentEnv hosting only one "
                "type of agent but with several copies."
            )
        env = ExternalEnvWrapper(self)

        return env


class _ExternalEnvEpisode:
    """Tracked state for each active episode."""

    def __init__(
        self,
        episode_id: str,
        results_avail_condition: threading.Condition,
        training_enabled: bool,
        multiagent: bool = False,
    ):
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


class ExternalEnvWrapper(BaseEnv):
    """Internal adapter of ExternalEnv to BaseEnv."""

    def __init__(
        self, external_env: "ExternalEnv", preprocessor: "Preprocessor" = None
    ):
        from ray.rllib.env.external_multi_agent_env import ExternalMultiAgentEnv

        self.external_env = external_env
        self.prep = preprocessor
        self.multiagent = issubclass(type(external_env), ExternalMultiAgentEnv)
        self._action_space = external_env.action_space
        if preprocessor:
            self._observation_space = preprocessor.observation_space
        else:
            self._observation_space = external_env.observation_space
        external_env.start()

    @override(BaseEnv)
    def poll(
        self,
    ) -> Tuple[MultiEnvDict, MultiEnvDict, MultiEnvDict, MultiEnvDict, MultiEnvDict]:
        with self.external_env._results_avail_condition:
            results = self._poll()
            while len(results[0]) == 0:
                self.external_env._results_avail_condition.wait()
                results = self._poll()
                if not self.external_env.is_alive():
                    raise Exception("Serving thread has stopped.")
        limit = self.external_env._max_concurrent_episodes
        assert len(results[0]) < limit, (
            "Too many concurrent episodes, were some leaked? This "
            "ExternalEnv was created with max_concurrent={}".format(limit)
        )
        return results

    @override(BaseEnv)
    def send_actions(self, action_dict: MultiEnvDict) -> None:
        from ray.rllib.env.base_env import _DUMMY_AGENT_ID

        if self.multiagent:
            for env_id, actions in action_dict.items():
                self.external_env._episodes[env_id].action_queue.put(actions)
        else:
            for env_id, action in action_dict.items():
                self.external_env._episodes[env_id].action_queue.put(
                    action[_DUMMY_AGENT_ID]
                )

    def _poll(
        self,
    ) -> Tuple[MultiEnvDict, MultiEnvDict, MultiEnvDict, MultiEnvDict, MultiEnvDict]:
        from ray.rllib.env.base_env import with_dummy_agent_id

        all_obs, all_rewards, all_dones, all_infos = {}, {}, {}, {}
        off_policy_actions = {}
        for eid, episode in self.external_env._episodes.copy().items():
            data = episode.get_data()
            cur_done = (
                episode.cur_done_dict["__all__"]
                if self.multiagent
                else episode.cur_done
            )
            if cur_done:
                del self.external_env._episodes[eid]
            if data:
                if self.prep:
                    all_obs[eid] = self.prep.transform(data["obs"])
                else:
                    all_obs[eid] = data["obs"]
                all_rewards[eid] = data["reward"]
                all_dones[eid] = data["done"]
                all_infos[eid] = data["info"]
                if "off_policy_action" in data:
                    off_policy_actions[eid] = data["off_policy_action"]
        if self.multiagent:
            # Ensure a consistent set of keys
            # rely on all_obs having all possible keys for now.
            for eid, eid_dict in all_obs.items():
                for agent_id in eid_dict.keys():

                    def fix(d, zero_val):
                        if agent_id not in d[eid]:
                            d[eid][agent_id] = zero_val

                    fix(all_rewards, 0.0)
                    fix(all_dones, False)
                    fix(all_infos, {})
            return (all_obs, all_rewards, all_dones, all_infos, off_policy_actions)
        else:
            return (
                with_dummy_agent_id(all_obs),
                with_dummy_agent_id(all_rewards),
                with_dummy_agent_id(all_dones, "__all__"),
                with_dummy_agent_id(all_infos),
                with_dummy_agent_id(off_policy_actions),
            )

    @property
    @override(BaseEnv)
    @PublicAPI
    def observation_space(self) -> gym.spaces.Dict:
        return self._observation_space

    @property
    @override(BaseEnv)
    @PublicAPI
    def action_space(self) -> gym.Space:
        return self._action_space

if __name__ == "__main__":

    config = {'Folder_Output': '',
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
        'ruta': 'A' # A-Notebook Lenovo, B-Notebook Asus, C-Computadora grupo
        }

    from ray.tune import register_env
    from ray.rllib.agents.dqn import DQNTrainer
    YourExternalEnv = ExternalEnv
    register_env("EP_Env",
        ExternalEnv(config))

    trainer = DQNTrainer(env="EP_Env")
    
    while True:
        print(trainer.train())