from typing import Dict
import ray
from ray import tune
from ray.rllib.agents.ppo.ppo import PPOTrainer
from ray.tune.logger import pretty_print
from ray.tune.registry import register_env

from gym.spaces import Discrete, Box

from EPRLlib_ExtEnv import EnergyPlusEnv

def env_creator(config: Dict):
    action_space = Discrete(32)
    observation_space = Box(float("-inf"), float("inf"), (7,))
    return EnergyPlusEnv(action_space, observation_space)

if __name__ == "__main__":
    
    ray.init()

    register_env("TEE", env_creator)

    trainer = PPOTrainer(config= {"framework": "tf2"}, env="TEE")
    results = tune.run()
    pretty_print(results)
    print("Training end")