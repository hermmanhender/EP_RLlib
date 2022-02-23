import ray
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