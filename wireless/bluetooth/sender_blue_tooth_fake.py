import requests
from wireless.sender import Sender


class SenderBlueToothFake(Sender):

    def send(self, url, json: dict):
        requests.post(url, json=json)
