from common.utils import get_data, send_data
import json
from common.settings import *
from client import presence, connect_to_server
from server import run_server
from unittest import TestCase


class TestUtils(TestCase):
    def setUp(self):
        self.message = presence()
        self.enc_message = json.dumps(self.message).encode(ENCODING)
        self.sock_server = run_server()
        self.sock_client = connect_to_server()
        self.client, addr = self.sock_server.accept()

    def test_get_data(self):
        self.client.send(self.enc_message)
        self.assertEqual(get_data(self.sock_client), self.message)

    def test_send_data(self):
        send_data(self.message, self.client)
        received_data = self.sock_client.recv(MAX_PACKAGE)
        self.assertEqual(self.enc_message, received_data)
