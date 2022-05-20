








parser = argparse.ArgumentParser()
parser.add_argument(
    "--no-train",
    action="store_true",
    help="Whether to disable training."
)
parser.add_argument(
    "--inference-mode",
    type=str,
    default="local",
    choices=["local", "remote"]
)
parser.add_argument(
    "--off-policy",
    action="store_true",
    help="Whether to compute random actions instead of on-policy "
    "(Policy-computed) ones.",
)
parser.add_argument(
    "--stop-reward",
    type=float,
    default=9999,
    help="Stop once the specified reward is reached.",
)
parser.add_argument(
    "--port",
    type=int,
    default=9900,
    help="The port to use (on localhost)."
)

config = {'Folder_Output': '',
        'Weather_file': '',
        'epJSON_file': '',
        'episode': 0,
        'last_observation': [],
        'T_SP': 24.,
        'dT_up': 1.,
        'dT_dn': 4.,
        'SP_RH': 70.,
        'nombre_caso': "rho10-100", # Se utiliza para identificar la carpeta donde se guardan los datos
        'rho': 10, # Temperatura: default: 0.25
        'beta': 1, # Energía: default: 20
        'psi': 0, # Humedad relativa: default: 0.005
        'first_time_step': True,
        'directorio': '',
        'ruta_base': 'C:/Users/grhen/Documents/GitHub/RLforEP',
        'ruta': 'A' # A-Notebook Lenovo, B-Notebook Asus, C-Computadora grupo
        }

if __name__ == "__main__":
    args = parser.parse_args()

    client = PolicyClient(
        f"http://localhost:{args.port}",
        inference_mode=args.inference_mode
        )
    
    environment()

    n = 0
    while n < 1000:
        print("\nEpisode "+ str(n+1))
        environment.run(environment)
        n += 1

    from ray.tune import register_env
    from ray.rllib.algorithms.dqn import DQNTrainer # doctest: +SKIP
    YourExternalEnv = ... # doctest: +SKIP
    register_env("my_env", # doctest: +SKIP
        lambda config: YourExternalEnv(config))
    trainer = DQNTrainer(env="my_env") # doctest: +SKIP
    while True: # doctest: +SKIP
        print(trainer.train()) # doctest: +SKIP