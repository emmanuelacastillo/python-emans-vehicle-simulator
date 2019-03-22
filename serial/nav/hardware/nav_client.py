"""
NavClient is an interface for access
navigation data from a navigation
system. This interface will allow
different implementation if a new
navigation requires a different way
to access its data.

"""


from abc import ABC, abstractmethod


class NavClient(ABC):

    @abstractmethod
    def receive(self, data: bytearray):
        pass # construct based on protocol