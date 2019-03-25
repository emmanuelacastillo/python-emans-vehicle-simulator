from serial.can.hardware.can_client_fake_data import CanClientFakeData
import time
from wireless.sender_facade import SenderFacade

__READ_BUS_SECONDS: int = 60
__FAKE_CAN_LOC: str = 'C:\\Users\\emman\\Desktop\\projects\\python-emans-vehicle-simulator\\data\\fakecandata.csv'
__VEHICLE_INFO_URL: str = 'http://localhost:5000/eld/vehicle/info'
__VEHICLE_WARNING_URL: str = 'http://localhost:5000/eld/vehicle/warning'


def run_can_main():
    time.sleep(1)
    print("Work Login")
    print(".............")
    print("Name: Bob Bobby")
    print("Start Time: ")
    print("Destination")
    print("...............")
    print("Address: 1234 Test St.")
    print("City: Test City")
    print("State: Test State")
    print("Zip Code: 92069")
    print("**Engine Started**")
    time.sleep(1)

    for data_index in range(__READ_BUS_SECONDS):
        time.sleep(1)
        general_data, warning_data = CanClientFakeData(__FAKE_CAN_LOC).receive(data_index)
        SenderFacade.post_data(__VEHICLE_INFO_URL, json=general_data.get_json())
        if data_index % 5 == 0:
            SenderFacade.post_data(__VEHICLE_WARNING_URL, json=warning_data.get_json())

    print("**Engine Stoped**")
