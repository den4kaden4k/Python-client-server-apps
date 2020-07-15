from socket import socket, AF_INET, SOCK_STREAM
from select import select
import json
from common.settings import MAX_CONNECTIONS, DEFAULT_IP, DEFAULT_PORT, ENCODING, MAX_PACKAGE
from common.utils import get_time
from common.decorators import log
from log.config_log_server import LOGGER


@log(LOGGER)
def join_user(data):
    log_message = f'{get_time()}: {data["address"]}: <{data["name"]}> присоединился к чату'
    print(log_message)
    LOGGER.debug(log_message)
    return f'{get_time()}: {data["name"]} присоединился к чату'


@log(LOGGER)
def left_user(user):
    log_message = f'{get_time()}: Клиент {user.getpeername()} <{sock_to_name[user]}> отключился'
    print(log_message)
    LOGGER.debug(log_message)
    mes = {user: f'{get_time()}: {sock_to_name[user]} покинул чат'}
    sock_to_name.pop(user)
    clients.remove(user)
    user.close()
    send_message(mes, clients)


def message(data):
    print(f'{get_time()}: {data["address"]}: <{data["name"]}>: {data["value"]}')
    return f'{get_time()}: {data["name"]} >>> {data["value"]}'


def get_message(r_clients):
    msg = {}
    for client in r_clients:
        try:
            data = json.loads(client.recv(MAX_PACKAGE).decode(ENCODING))
            msg[client] = data
        except ConnectionResetError:
            left_user(client)
    return msg


@log(LOGGER)
def send_message(message_to_send: dict, w_clients):
    for sender, value in message_to_send.items():
        for w_client in w_clients:
            if w_client != sender:
                try:
                    w_client.send(value.encode(ENCODING))
                except ConnectionResetError:
                    left_user(w_client)


sock_to_name = {}
clients = []


def main():
    join_addr = ''
    address = (DEFAULT_IP, DEFAULT_PORT)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(MAX_CONNECTIONS)
    sock.settimeout(0.2)
    mes = f'{get_time()}: [Server started]'
    print(mes)
    LOGGER.debug(mes)
    action = {
        'presence': join_user,
        'message': message,
    }
    while True:
        try:
            client, join_addr = sock.accept()
            clients.append(client)
        except OSError:
            pass
        finally:
            r, w = [], []
            try:
                r, w, e = select(clients, clients, [], 0)
            except:
                pass
            request = get_message(r)
            if request:
                for sock_r, data_r in request.items():
                    response = {}
                    data_r['address'] = join_addr
                    act = data_r['action']
                    response_data = action[act](data_r)
                    response[sock_r] = response_data
                    if sock_r not in sock_to_name:
                        sock_to_name[sock_r] = data_r['name']
                    send_message(response, w)


if __name__ == '__main__':
    main()
