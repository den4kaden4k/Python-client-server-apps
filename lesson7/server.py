from socket import *
from select import select


def get_message(r_clients, all_clients):
    msg = {}
    for client in r_clients:
        try:
            data = client.recv(1024).decode('utf-8')
            msg[client] = data
        except:
            print(f'Клиент {client.fileno()} {client.getpeername()} отключился')
            all_clients.remove(client)
             # вывести в лог
    return msg


def send_message(message_to_send: dict, w_clients, all_clients):
    for sender, value in message_to_send.items():
        for w_client in w_clients:
            if w_client != sender:
                try:
                    w_client.send(value.encode('utf-8'))
                except:
                    print(f'Клиент {w_client.fileno()} {w_client.getpeername()} отключился')
                    w_client.close()
                    all_clients.remove(w_client)
                    # вывести в лог


address = ('localhost', 7777)
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(address)
sock.listen(5)
sock.settimeout(0.2)
clients = []
while True:
    try:
        client, addr = sock.accept()
        clients.append(client)
    except OSError:
        pass
    finally:
        wait = 1
        r = []
        w = []
        try:
            r, w, e = select(clients, clients, [], wait)
        except:
            pass
        request = get_message(r, clients)
        if request:
            send_message(request, w, clients)

