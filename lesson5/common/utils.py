import argparse
import json
from common.settings import *


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', default=DEFAULT_IP)
    parser.add_argument('-p', default=DEFAULT_PORT)
    args = parser.parse_args()
    return args.a, args.p


def get_data(sock):
    data = sock.recv(MAX_PACKAGE)
    if isinstance(data, bytes):
        data_dec = data.decode(ENCODING)
        json_data = json.loads(data_dec)
        if isinstance(json_data, dict):
            return json_data
        raise ValueError
    raise ValueError


def send_data(dic, sock):
    data = json.dumps(dic).encode(ENCODING)
    sock.send(data)
