from hardware.common.receiver import Receiver


class BlueToothReceiver(Receiver):

    def receive(self, data: bytearray):
        pass
        # Parse bytes
        # Construct message
        # Send message for processing