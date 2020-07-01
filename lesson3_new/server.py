from chat10.temp import *

from socket import *
import argparse
import time
import json

print(my_time())
g = 1


def coder(dic):
    return json.dumps(dic).encode('utf-8')


def decoder(byte):
    return json.loads(byte.decode('utf-8'))


def presence():
    return coder(dict(action='200', timestamp=time.time(), status='answer'))


def run_server(address, port):
    sock = socket(type=SOCK_STREAM)
    sock.bind((address, port))
    sock.listen(5)
    return sock


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', default='')
    parser.add_argument('-p', default=7777)
    args = parser.parse_args()
    client, addr = run_server(args.a, args.p).accept()
    print(f'Соединение установлено: {addr}')
    action_list = {
        'authenticate': 'authenticate',
        'presence': presence(),
        'quit': 'quit',
    }
    try:
        while True:
            data = client.recv(1024)
            if data:
                key = decoder(data)['action']
                answer = action_list[key]
                client.send(answer)
                break
    finally:
        client.close()


if __name__ == '__main__':
    main()
