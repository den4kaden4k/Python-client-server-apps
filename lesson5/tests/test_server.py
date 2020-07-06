from server import run_server
from unittest import TestCase
import socket


class TestUtils(TestCase):
    def setUp(self):
        pass

    def test_run_server(self):
        self.assertIsInstance(run_server(), socket.socket)
