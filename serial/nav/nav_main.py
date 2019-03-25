from serial.nav.hardware.nav_client_fake_data import NavClientFakeData
import time
from wireless.sender_facade import SenderFacade

__READ_BUS_SECONDS: int = 60
__FAKE_NAV_LOC: str = 'C:\\Users\\emman\\Desktop\\projects\\python-emans-vehicle-simulator\\data\\fakenavdata.csv'
__NAV_INFO_URL: str = 'http://localhost:5000/eld/navigation/info'


def run_nav_main():
    time.sleep(1)
    print("**Navigation Initialized**")
    time.sleep(1)

    for data_index in range(__READ_BUS_SECONDS):
        time.sleep(1)
        nav_data = NavClientFakeData(__FAKE_NAV_LOC).receive(data_index)
        SenderFacade.post_data(__NAV_INFO_URL, json=nav_data.get_json())

    print("**Navigation Completed**")
