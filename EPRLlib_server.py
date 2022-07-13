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


#from hyperopt import hp

#from ray.tune.suggest.hyperopt import HyperOptSearch


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
        default=0,
        help="The number of workers to use. Each worker will create "
        "its own listening socket for incoming experiences.",
    )
    parser.add_argument(
        "--no-restore",
        action="store_false",
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
        default=30000,
        help="Number of iterations to train."
    )
    parser.add_argument(
        "--stop-timesteps",
        type=int,
        default=200000,
        help="Number of timesteps to train.",
    )
    
    parser.add_argument(
        "--as-test",
        action="store_true",
        help="Whether this script should be run as a test: --stop-reward must "
        "be achieved within --stop-timesteps AND --stop-iters.",
    )
    parser.add_argument(
        "--no-tune",
        action="store_false",
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

    # object_store_memory: The amount of memory (in bytes) to start the
    # object store with. By default, this is automatically set based on
    # available system memory.
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
        "action_space": spaces.Discrete(528), # son 5 accionables binarios y su combinatoria es 2^5
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
                # Number of rollout worker actors to create for parallel sampling. Setting
                # this to 0 will force rollouts to be done in the algorithm's actor.
                "num_workers": 0,
                "recreate_failed_workers": True,
                "replay_buffer_config": {
                    "learning_starts":100,
                    # Size of the replay buffer. Note that if async_updates is set,
                    # then each worker will have a replay buffer of this size.
                    "capacity": 50000,
                    },
                "timesteps_per_iteration": 100,
                "n_step": 30, # Tamaño del bache de datos
                "lr": 0.001,
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
                "train_batch_size": 4800,
            }
        )

    #checkpoint_path = CHECKPOINT_FILE.format(args.run)
    
    
    
    """# Attempt to restore from checkpoint, if possible.
    if not args.no_restore and os.path.exists(checkpoint_path):
        checkpoint_path = open(checkpoint_path).read()
    else:
        checkpoint_path = None"""

    # Manual training loop (no Ray tune).
    if args.no_tune:
        if args.run == "DQN":
            trainer = DQNTrainer(config=config)
        else:
            trainer = PPOTrainer(config=config)

        # if checkpoint_path:
        checkpoint_path = 'C:/Users/grhen/ray_results/DQNTrainer_None_2022-07-06_22-30-47ouzsz8q_/checkpoint_001847/checkpoint-1847'
        print("Restoring from checkpoint path", checkpoint_path)
        trainer.restore(checkpoint_path)
        
        # Serving and training loop.
        ts = 0
        for _ in range(args.stop_iters):
            results = trainer.train()
            print(pretty_print(results))
            checkpoint = trainer.save()
            print("Last checkpoint", checkpoint)
            """with open(checkpoint_path, "w") as f:
                f.write(checkpoint)
            if (
                results["episode_reward_mean"] >= args.stop_reward
                or ts >= args.stop_timesteps
            ):
                break"""
            ts += results["timesteps_total"]

    # Run with Tune for auto env and trainer creation and TensorBoard.
    else:
        """
        # How to stop Tune runs programmatically?
        We’ve just covered the case in which you manually interrupt a Tune run. But you can also
        control when trials are stopped early by passing the stop argument to tune.run. This argument
        takes, a dictionary, a function, or a Stopper class as an argument.

        If a dictionary is passed in, the keys may be any field in the return result of tune.report in
        the Function API or step() (including the results from step and auto-filled metrics).
        
        ## Stopping with a dictionary
        In the example below, each trial will be stopped either when it completes 10 iterations or
        when it reaches a mean accuracy of 0.98. These metrics are assumed to be increasing.
        
        # training_iteration is an auto-filled metric by Tune.
        tune.run(
            my_trainable,
            stop={"training_iteration": 10, "mean_accuracy": 0.98}
        )

        More in https://docs.ray.io/en/master/tune/tutorials/tune-stopping.html
        """
        stop = {
            "training_iteration": args.stop_iters,
            "timesteps_total": args.stop_timesteps,
            #"mean_accuracy": 0.98,
        }
        print("Se realiza un tuneo de los parametros.")

        # configure how checkpoints are sync'd to the scheduler/sampler
        sync_config = tune.SyncConfig()  # the default mode is to use use rsync

        #space = {
        #    "lr": hp.loguniform("lr", 1e-10, 0.1)
        #    }
        
        #hyperopt_search = HyperOptSearch(space, metric="mean_accuracy", mode="max")

        # To enable GPUs, use this instead:
        # analysis = tune.run(
        #     train_mnist, config=search_space, resources_per_trial={'gpu': 1})

        config.update({"lr": 0.01})

        analysis = tune.run(
            args.run,
            config=config,
            stop=stop,
            verbose=2,
            #metric="mean_accuracy",

            #search_alg=hyperopt_search,

            # if you would like to collect the stream outputs in files for later analysis or
            # troubleshooting, Tune offers an utility parameter, log_to_file, for this.
            log_to_file=True,

            # restore=checkpoint_path,

            # name of your experiment
            name="experimento_1",

            # a directory where results are stored before being
            # sync'd to head node/cloud storage
            local_dir="/tmp/mypath",

            # sync our checkpoints via rsync
            # you don't have to pass an empty sync config - but we
            # do it here for clarity and comparison
            sync_config=sync_config,

            # we'll keep the best five checkpoints at all times
            # checkpoints (by AUC score, reported by the trainable, descending)
            checkpoint_score_attr="max-auc",
            keep_checkpoints_num=5,

            # a very useful trick! this will resume from the last run specified by
            # sync_config (if one exists), otherwise it will start a new tuning run
            resume=False, #True, False, to resume the experiment or not, or AUTO, which will attempt to resume the experiment if possible, and otherwise will start a new experiment.
            )
        
        """
        # Analyses
        tune.run returns an ExperimentAnalysis object which has methods you can use for analyzing
        your training. The following example shows you how to access various metrics from an analysis
        object, like the best available trial, or the best hyperparameter configuration for that trial:
        """
        best_trial = analysis.get_best_trial()  # Get best trial
        best_config = analysis.get_best_config()  # Get best trial's hyperparameters
        best_logdir = analysis.get_best_logdir()  # Get best trial's logdir
        best_checkpoint = analysis.get_best_checkpoint(best_trial)  # Get best trial's best checkpoint
        best_result = analysis.get_best_trial().last_result  # Get best trial's last results
        best_result_df = analysis.get_best_trial().last_result  # Get best result as pandas dataframe
        
        best_result_df.to_csv(config['directorio'] + '/Resultados/best_result.csv', mode="w", index=False, header=False)

        """
        This object can also retrieve all training runs as dataframes, allowing you to do ad-hoc
        data analysis over your results.
        """
        # Get a dataframe with the last results for each trial
        df_results = analysis.results_df

        # Get a dataframe of results for a specific score or mode
        df = analysis.dataframe(metric="score", mode="max")



        if args.run == "DQN":
            trainer = DQNTrainer(config=config)
        else:
            trainer = PPOTrainer(config=config)

        print("Restoring from the best checkpoint path", best_checkpoint)
        trainer.restore(best_checkpoint)

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