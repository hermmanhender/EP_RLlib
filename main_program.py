import ray
from ray import tune
import gym
import EPrun

ray.init()
tune.run(
    "PPO",
    config={
        "env": None,
        "observation_space": gym.spaces.Box(float("-inf"), float("inf"), (4,)),
        "action_space": gym.spaces.Discrete(2)
    }
)

