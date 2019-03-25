"""
CanClient is an interface that access data
from the CAN bus. This interface allows
different protocols that can be implemented
to access data from the CAN bus.

"""
from abc import ABC, abstractmethod


class CanClient(ABC):

    @abstractmethod
    def receive(self, data_index: int = None):
        pass # construct based on protocol