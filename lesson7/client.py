from socket import *
from select import select
import time
import random


def send_message(mes):
    s.send(mes.encode('utf-8'))


def read_message():
    s.recv(1024).decode('utf-8')


address = 'localhost'
port = 7777
s = socket(AF_INET, SOCK_STREAM)
s.connect((address, port))

while True:
    try:
        message = input()
        send_message(message)

    except:
        pass
