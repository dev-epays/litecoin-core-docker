import os

args = {'rpcuser': os.getenv("RPC_USER", "admin"),
        'rpcpassword': os.getenv("RPC_PASSWORD", "admin"),
        'rpcbind': os.getenv("RPC_BIND", "0.0.0.0").split(";"),
        'rpcallowip': os.getenv("RPC_ALLOW_IP", "0.0.0.0/0.0.0.0").split(";"),
        'printtoconsole': '',
        'txindex': os.getenv("TX_INDEX", "1")}

CORE_PATH = f"/usr/local/bin/{os.getenv('CORE_NAME')}d"

args_list = []
for key in args:
    value = args.get(key)
    if isinstance(value, list):
        for element in value:
            args_list.append(f"-{key}={element}")
    elif value:
        args_list.append(f"-{key}={value}")
    else:
        args_list.append(f"-{key}")

args_list = [CORE_PATH] + args_list
os.execl(CORE_PATH, *args_list)
