from wireless.sender import Sender


class SenderModemFake(Sender):

    def send(self, data: bytearray):
        pass # construct based on protocol