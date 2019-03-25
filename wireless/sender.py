from abc import ABC, abstractmethod


class Sender(ABC):

    @abstractmethod
    def send(self, url, json: dict):
        pass
