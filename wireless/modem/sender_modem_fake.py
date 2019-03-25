import requests
from wireless.sender import Sender


class SenderModemFake(Sender):

    def send(self, url, json: dict):
        requests.post(url, json=json)