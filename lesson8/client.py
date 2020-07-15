from socket import socket, AF_INET, SOCK_STREAM
import time
from threading import Thread
import json
from common.settings import ENCODING, MAX_PACKAGE, DEFAULT_IP, DEFAULT_PORT, MAX_TRYING, DEFAULT_USER
from common.utils import get_date_time
from common.decorators import log
from log.config_log_client import LOGGER


def presence(_name):
    return dict(action='presence', timestamp=get_date_time(), name=_name)


def message(mes, _name):
    return dict(action='message', timestamp=get_date_time(), value=mes, name=_name)


@log(LOGGER)
def send_message(mes, s):
    try:
        s.send(json.dumps(mes).encode(ENCODING))
        return 1
    except (ConnectionResetError, ConnectionRefusedError) as e:
        log_message = f'{get_date_time()}: Сервер недоступен'
        print(log_message)
        LOGGER.critical(e)
        return 0


@log(LOGGER)
def read_message(s):
    while True:
        try:
            msg = s.recv(MAX_PACKAGE).decode(ENCODING)
            print(msg)
        except (ConnectionResetError, ConnectionRefusedError) as e:
            log_message = f'{get_date_time()}: Сервер недоступен.'
            print(f'{log_message} Нажмите Enter для продолжения.')
            LOGGER.critical(e)
            break


@log(LOGGER)
def try_connect():
    address = (DEFAULT_IP, DEFAULT_PORT)
    s = socket(AF_INET, SOCK_STREAM)
    count = 0
    while count < MAX_TRYING:
        try:
            s.connect(address)
            mes = f'Установлено соединение с сервером {address}'
            print(mes)
            LOGGER.debug(mes)
            return s
        except (ConnectionRefusedError, ConnectionResetError):
            count += 1
            print(f'Повторное подключение... (осталось {MAX_TRYING - count} попыток)')
            time.sleep(1)
            continue
    s.close()
    return 0


_name = input('Введи свой ник: ')
if not _name.split():
    _name = DEFAULT_USER


def main():
    while True:
        sock = try_connect()
        if not sock:
            next_step = input('Не удалось подключиться к серверу. Повторить попытку? '
                              '(yes - повторить, no - выйти из программы)\n')
            if next_step == 'yes':
                continue
            else:
                LOGGER.debug('Выход из программы после неудачного соединения с сервером')
                break
        tr = Thread(target=read_message, args=(sock,))
        tr.start()
        check_online = send_message(presence(_name), sock)
        while check_online and tr.is_alive():
            try:
                input_msg = input()
                if input_msg.split() and tr.is_alive():
                    check_online = send_message(message(input_msg, _name), sock)
                elif not tr.is_alive():
                    break
            except Exception as e:
                LOGGER.critical(e)
                break
        tr.join()
        sock.close()


if __name__ == '__main__':
    main()
