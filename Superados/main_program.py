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
from cmath import inf
import numpy as np
from typing import Dict
import ray
from ray.rllib.agents.ppo.ppo import PPOTrainer
from ray.tune.logger import pretty_print
from ray.tune.registry import register_env

from gym.spaces import Discrete, Box

from Superados.EnergyPlus_external_env import EPExternalEnv

def env_creator():
    action_space = Discrete(2)
    observation_space = Box(-np.Inf, np.Inf, (7,))
    
    return EPExternalEnv(
                 action_space = action_space,
                 observation_space = observation_space,
                 )

if __name__ == "__main__":
    
    ray.init()

    register_env("TEE", env_creator())

    trainer = PPOTrainer(config= {"framework": "tf2"}, env="TEE")
    results = trainer.train()
    pretty_print(results)
    print("Training end")