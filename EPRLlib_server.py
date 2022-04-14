"""
# RLlib Server

Running an RLlib policy server, allowing connections from external environment
running clients. The server listens on against an RLlib policy server listening
on one or more HTTP-speaking ports. See `EPRLlib_client.py` in this same directory for how
to start any number of clients (after this server has been started).


Setup:
1) Start this server:
    $ python EPRLlib_server.py --num-workers --[other options]
      Use --help for help.
2) Run n policy clients:
    See `EPRLlib_client.py` on how to do this.

The `num-workers` setting will allow you to distribute the incoming feed over n
listen sockets (in this example, between 9900 and 990n with n=worker_idx-1).
You may connect more than one policy client to any open listen port.
"""
# Importacion de la libreria argparse que sirve para la configuracion
# de los parametros del Trainer y del servidor
import argparse
# Se importa spaces de gym para poder definir luego el tamaño de los espacios
# de observaciones y acciones del entorno, ya que al utilizar un cliente
# externo es necesario definirlo aqui en el servidor
from gym import spaces
# La libreria os se utilizara para la creacion de directorios donde se almacenaran
# los archivos de datos y configuracion del experimento
import os
# Ray es la libreria principal de la cual se obtiene la preconfiguracion del 
# servidor y los clientes.
# Todos sus modulos luego importados son utilizados para la configuracion del servidor,
# el que contiene a los Trainers, Policy y la herramienta Tune para hacer un tunning de
# los hiperparametros
import ray
from ray import tune
from ray.rllib.agents.dqn import DQNTrainer
from ray.rllib.agents.ppo import PPOTrainer
from ray.rllib.env.policy_server_input import PolicyServerInput
from ray.rllib.examples.custom_metrics_and_callbacks import MyCallbacks
from ray.tune.logger import pretty_print

# Se define la direccion del servidor. Se puede indicar un IP o bien con
# el comando "localhost" definir el IP local, el cual lo busca automaticamente
SERVER_ADDRESS = "localhost"
# In this example, the user can run the policy server with
# n workers, opening up listen ports 9900 - 990n (n = num_workers - 1)
# to each of which different clients may connect.
SERVER_BASE_PORT = 9900  # + worker-idx - 1
# ¿?
CHECKPOINT_FILE = "last_checkpoint_{}.out"


def get_cli_args():
    """
    # Trainer configuration
    
    Create CLI (Comand Line Interface) parser and return parsed arguments.
    
    They manage algorithm configuration, setup of the rollout workers and optimizer,
    and collection of training metrics. Trainers also implement the Tune Trainable
    API for easy experiment management.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--port",
        type=int,
        default=SERVER_BASE_PORT,
        help="The base-port to use (on localhost). " f"Default is {SERVER_BASE_PORT}.",
    )
    parser.add_argument(
        "--callbacks-verbose",
        action="store_true",
        help="Activates info-messages for different events on "
        "server/client (episode steps, postprocessing, etc..).",
    )

    # Number of rollout worker actors to create for parallel sampling. Setting
    # this to 0 will force rollouts to be done in the trainer actor.
    parser.add_argument(
        "--num-workers",
        type=int,
        default=4,
        help="The number of workers to use. Each worker will create "
        "its own listening socket for incoming experiences.",
    )
    parser.add_argument(
        "--no-restore",
        action="store_true",
        help="Do not restore from a previously saved checkpoint (location of "
        "which is saved in `last_checkpoint_[algo-name].out`).",
    )

    # General args.
    parser.add_argument(
        "--run",
        default="DQN",
        choices=["DQN", "PPO"],
        help="The RLlib-registered algorithm to use.",
    )
    parser.add_argument(
        "--num-cpus",
        type=int,
        default=8
    )

    # tf: TensorFlow (static-graph)
    # tf2: TensorFlow 2.x (eager or traced, if eager_tracing=True)
    # tfe: TensorFlow eager (or traced, if eager_tracing=True)
    # torch: PyTorch
    parser.add_argument(
        "--framework",
        choices=["tf", "tf2", "tfe", "torch"],
        default="tf",
        help="The DL framework specifier.",
    )
    parser.add_argument(
        "--stop-iters",
        type=int,
        default=4800,
        help="Number of iterations to train."
    )
    parser.add_argument(
        "--stop-timesteps",
        type=int,
        default=50000000,
        help="Number of timesteps to train.",
    )
    parser.add_argument(
        "--stop-reward",
        type=float,
        default=10000.0,
        help="Reward at which we stop training.",
    )
    parser.add_argument(
        "--as-test",
        action="store_true",
        help="Whether this script should be run as a test: --stop-reward must "
        "be achieved within --stop-timesteps AND --stop-iters.",
    )
    parser.add_argument(
        "--no-tune",
        action="store_true",
        help="Run without Tune using a manual train loop instead. Here,"
        "there is no TensorBoard support.",
    )
    parser.add_argument(
        "--local-mode",
        action="store_true",
        help="Init Ray in local mode for easier debugging.",
    )

    parser.add_argument(
        "--checkpoint-freq",
        default=2400,
        help="In order to save checkpoints from which to evaluate policies",
    )

    # Number of GPUs to allocate to the trainer process. Note that not all
    # algorithms can take advantage of trainer GPUs. Support for multi-GPU
    # is currently only available for tf-[PPO/IMPALA/DQN/PG].
    # This can be fractional (e.g., 0.3 GPUs).
    parser.add_argument(
        "--num_gpus",
        default=0,
        help="In order to use the GPU. If set in 0, you use the CPU",
    )

    args = parser.parse_args()
    print(f"Running with following CLI args: {args}")
    return args


if __name__ == "__main__":
    # Se inicia la configuracion, la cual fue definida anteriormente
    args = get_cli_args()
    # Se inicia el servidor con ray
    ray.init()

    # `InputReader` generator (returns None if no input reader is needed on
    # the respective worker).
    def _input(ioctx):
        # We are remote worker or we are local worker with num_workers=0:
        # Create a PolicyServerInput.
        if ioctx.worker_index > 0 or ioctx.worker.num_workers == 0:
            return PolicyServerInput(
                ioctx,
                SERVER_ADDRESS,
                args.port + ioctx.worker_index - (1 if ioctx.worker_index > 0 else 0),
            )
        # No InputReader (PolicyServerInput) needed.
        else:
            return None


    # Trainer config. Note that this config is sent to the client only in case
    # the client needs to create its own policy copy for local inference.
    config = {
        # Indicate that the Trainer we setup here doesn't need an actual env.
        # Allow spaces to be determined by user (see below).
        "env": None,
        # TODO: (sven) make these settings unnecessary and get the information
        #  about the env spaces from the client.
        "observation_space": spaces.Box(float("-inf"), float("inf"), (7,)),
        "action_space": spaces.Discrete(16),
        # Use the `PolicyServerInput` to generate experiences.
        "input": _input,
        # Use n worker processes to listen on different ports.
        "num_workers": args.num_workers,
        # Disable OPE, since the rollouts are coming from online clients.
        "input_evaluation": [],
        # Create a "chatty" client/server or not.
        "callbacks": MyCallbacks if args.callbacks_verbose else None,
        # DL framework to use.
        "framework": args.framework,
        # Set to INFO so we'll see the server's actual address:port.
        "log_level": "INFO",
    }

    # DQN.
    if args.run == "DQN":
        # Example of using DQN (supports off-policy actions).
        config.update(
            {
                "learning_starts": 100,
                "timesteps_per_iteration": 200,
                "n_step": 4,
            }
        )
        config["model"] = {
            "fcnet_hiddens": [64],
            "fcnet_activation": "linear",
        }

    # PPO.
    else:
        # Example of using PPO (does NOT support off-policy actions).
        config.update(
            {
                "rollout_fragment_length": 1000,
                "train_batch_size": 4000,
            }
        )

    checkpoint_path = CHECKPOINT_FILE.format(args.run)
    # Attempt to restore from checkpoint, if possible.
    if not args.no_restore and os.path.exists(checkpoint_path):
        checkpoint_path = open(checkpoint_path).read()
    else:
        checkpoint_path = None

    # Manual training loop (no Ray tune).
    if args.no_tune:
        if args.run == "DQN":
            trainer = DQNTrainer(config=config)
        else:
            trainer = PPOTrainer(config=config)

        if checkpoint_path:
            print("Restoring from checkpoint path", checkpoint_path)
            trainer.restore(checkpoint_path)

        # Serving and training loop.
        ts = 0
        for _ in range(args.stop_iters):
            results = trainer.train()
            print(pretty_print(results))
            checkpoint = trainer.save()
            print("Last checkpoint", checkpoint)
            with open(checkpoint_path, "w") as f:
                f.write(checkpoint)
            if (
                results["episode_reward_mean"] >= args.stop_reward
                or ts >= args.stop_timesteps
            ):
                break
            ts += results["timesteps_total"]

    # Run with Tune for auto env and trainer creation and TensorBoard.
    else:
        stop = {
            "training_iteration": args.stop_iters,
            "timesteps_total": args.stop_timesteps,
            "episode_reward_mean": args.stop_reward,
        }
        print("Se realiza un tuneo de los parametros.")
        tune.run(args.run, config=config, stop=stop, verbose=2, restore=checkpoint_path)