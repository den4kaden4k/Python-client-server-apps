from client import connect_to_server
from server import run_server
from unittest import TestCase
import socket


class TestUtils(TestCase):
    def setUp(self):
        pass

    def test_connect_to_server(self):
        sock_server = run_server()
        sock = connect_to_server()
        sock_server.accept()
        self.assertIsInstance(sock, socket.socket)
