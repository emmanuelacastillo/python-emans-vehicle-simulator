from serial.can.hardware.can_client import CanClient


class CanClientFakeData(CanClient):

    def receive(self, data: bytearray):
        pass  # construct based on protocol