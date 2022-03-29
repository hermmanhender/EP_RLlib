from ray.tune import register_env
from ray.rllib.agents.dqn import DQNTrainer
from gym import spaces
from EPExternalEnv import ExternalEnv

YourExternalEnv = ExternalEnv
register_env("my_env",
    lambda config: YourExternalEnv(action_space=spaces.Discrete(16),
                 observation_space=spaces.Box(low=float("-inf"), high=float("inf"), shape=(7,)))
            )
trainer = DQNTrainer(env="my_env")
while True:
    print(trainer.train())

