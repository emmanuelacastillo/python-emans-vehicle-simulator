from flask import Flask
from services.eld_service import start_eld_services
from services.fake_service import start_fake_data_services

_app = Flask(__name__)


def main_services():
    start_eld_services(_app)
    start_fake_data_services(_app)
    return _app
