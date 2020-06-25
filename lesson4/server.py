from socket import *
from common.utils import *
import time


def presence():
    return dict(action='200', timestamp=time.time(), status='answer')


def run_server():
    args = parse_args()
    sock = socket(type=SOCK_STREAM)
    sock.bind(args)
    sock.listen(MAX_CONNECTIONS)
    return sock


def main():
    client, addr = run_server().accept()
    print(f'Соединение установлено: {addr}')
    action_list = {
        'authenticate': 'authenticate',
        'presence': presence,
        'quit': 'quit',
    }
    data = get_data(client)
    key = data['action']
    if key in action_list:
        answer = action_list[data['action']]()
        send_data(answer, client)


if __name__ == '__main__':
    main()
