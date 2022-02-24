"""import ray
from ray import tune
import gym


from ray.tune.registry import register_env
import ray

register_env("my_env", lambda config: YourExternalEnv(config))
        >>> trainer = DQNTrainer(env="my_env")
        >>> while True:
        >>>     print(trainer.train())
ray.init()
tune.run(
    "DQN",
    config={
        "env": None,
        "observation_space": gym.spaces.Box(float("-inf"), float("inf"), (7,)),
        "action_space": gym.spaces.Discrete(2)
    }
)
"""
import numpy as np
from typing import Dict
import ray
from ray.rllib.agents.ppo.ppo import PPOTrainer
from ray.tune.logger import pretty_print
from ray.tune.registry import register_env

from gym.spaces import Discrete, Box

from EnergyPlus_external_env import EPExternalEnv

def env_creator():
    action_space = Discrete(2)
    observation_space = Box(-10, 10, (4,))
    config = {
                    'Folder_Output': '',
                    'Weather_file': '',
                    'epJSON_file': '',
                    'episode': 0,
                    'last_observation': np.zeros((7,),dtype=float),
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
                 }
    return EPExternalEnv(
                 action_space,
                 observation_space,
                 max_concurrent = 100,
                 config = config)

if __name__ == "__main__":
    
    ray.init()

    register_env("TEE", env_creator())

    trainer = PPOTrainer(config= {"framework": "tf2"}, env="TEE")
    results = trainer.train()
    pretty_print(results)
    print("Training end")