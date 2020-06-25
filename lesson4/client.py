from socket import *
import time
from common.utils import *


def presence():
    return dict(action='presence', timestamp=time.time(), user=dict(account_name=DEFAULT_ACCOUNT))


def msg():
    pass


def connect_to_server():
    args = parse_args()
    sock = socket(type=SOCK_STREAM)
    sock.connect(args)
    return sock


def main():
    sock = connect_to_server()
    list_actions = {
        'probe': presence,
        'msg': msg,
    }
    list_codes = {
        '200': 'ok'
    }
    send_data(presence(), sock)
    data = get_data(sock)
    key = data['action']
    if key in list_actions:
        action = list_actions[key]()
        send_data(action, sock)
    elif key in list_codes:
        print(key)


if __name__ == '__main__':
    main()
