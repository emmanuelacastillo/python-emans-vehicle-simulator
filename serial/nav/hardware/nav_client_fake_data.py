from serial.nav.hardware.nav_client import NavClient


class NavClientFakeData(NavClient):

    def receive(self, data: bytearray):
        pass # construct based on protocol