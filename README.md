# EP_RLlib
Repository where an Server/Client configuration of RLlib built from the EnergyPlus library is hosted. The Client contains the ExternalEnv or environment of EnergyPlus.

## EnergyPlus RLlib Server

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

## EnergyPlus RLlib Client (ExternalEnv)

Running an external simulator against an RLlib policy server listening on one or more
HTTP-speaking port(s). See `EPRLlib_server.py` in this same directory for
how to start this server.

Setup:
1) Start the policy server:
    See `EPRLlib_server.py` on how to do this.
2) Run this client:
    $ python EPRLlib_client.py --inference-mode=local|remote --[other options]
      Use --help for help.

In "local" inference-mode, the action computations are performed
inside the PolicyClient used in this script w/o sending an HTTP request
to the server. This reduces network communication overhead, but requires
the PolicyClient to create its own RolloutWorker (+Policy) based on
the server's config. The PolicyClient will retrieve this config automatically.
You do not need to define the RLlib config dict here!

In "remote" inference mode, the PolicyClient will send action requests to the
server and not compute its own actions locally. The server then performs the
inference forward pass and returns the action to the client.

In either case, the user of PolicyClient must:
- Declare new episodes and finished episodes to the PolicyClient.
- Log rewards to the PolicyClient.
- Call `get_action` to receive an action from the PolicyClient (whether it'd be
  computed locally or remotely).
- Besides `get_action`, the user may let the PolicyClient know about
  off-policy actions having been taken via `log_action`. This can be used in
  combination with `get_action`, but will only work, if the connected server
  runs an off-policy RL algorithm (such as DQN, SAC, or DDPG).
