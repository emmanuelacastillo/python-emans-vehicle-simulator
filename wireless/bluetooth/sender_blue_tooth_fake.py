from wireless.sender import Sender


class SenderBlueToothFake(Sender):

    def send(self, data: bytearray):
        pass # construct based on protocol