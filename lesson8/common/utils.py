import argparse
from datetime import datetime
import time
from common.settings import DEFAULT_IP, DEFAULT_PORT


def get_date_time():
    return str(datetime.now())


def get_time():
    return time.strftime('%X')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', default=DEFAULT_IP)
    parser.add_argument('-p', default=DEFAULT_PORT)
    args = parser.parse_args()
    return args.a, args.p
