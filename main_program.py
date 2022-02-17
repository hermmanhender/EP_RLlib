import ray
from ray import tune
import gym
from EnergyPlus_external_env import ExternalEnv

import ray

def _init():
    ExternalEnv.run(ExternalEnv)

ray.init()
tune.run(
    "DQN",
    config={
        "env": None,
        "observation_space": gym.spaces.Box(float("-inf"), float("inf"), (7,)),
        "action_space": gym.spaces.Discrete(2),
        'init': _init
    }
)


