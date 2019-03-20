from abc import ABC, abstractmethod


class Receiver(ABC):

    @abstractmethod
    def receive(self, data: bytearray):
        pass # construct based on protocol