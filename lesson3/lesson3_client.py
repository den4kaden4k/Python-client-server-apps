from socket import *
from datetime import datetime
import json
import time
import argparse


def coder(dic):
    return json.dumps(dic).encode('utf-8')


def decoder(byte):
    return json.loads(byte.decode('utf-8'))


def presence():
    return dict(action='presence', timestamp=datetime.timestamp(datetime.now()))


def msg():
    pass


def connect_to_server(ip, port):
    sock = socket(type=SOCK_STREAM)
    sock.connect((ip, port))
    return sock


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', default='localhost')
    parser.add_argument('-p', default=7777)
    args = parser.parse_args()
    sock = connect_to_server(args.a, args.p)
    list_actions = {
        'probe': presence(),
        '200': 'ok',
        'msg': msg(),
    }
    ans_to_server = ['probe']
    sock.send(coder(presence()))
    while True:
        data = sock.recv(1024)
        if data:
            key = decoder(data)['action']
            action = list_actions[key]
            print(key)
            if key in ans_to_server:
                sock.send(coder(action))
                print(f'Сообщение от сервера: , {key}')
        else:
            break


if __name__ == '__main__':
    main()
