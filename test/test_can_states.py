import unittest
from serial.can.can_main import can_run_hsm


class TestCanStates(unittest.TestCase):

    def test_can_run_hsm(self):
        can_run_hsm()


