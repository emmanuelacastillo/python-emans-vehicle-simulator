# Eman's Vehicle Simulator

This project is designed to simulate a vehicle driving and obtaining data from a
Controller Area Network (CAN) bus and a navigation system. This data is sent to a
REST service for processing. Data is collected from each system every second until
the drive to a destination is completed. The destination is set to be for 1 minute.

There are 3 types of data that is sent to its corresponding REST service endpoint:

1. General Vehicle Information which consist of: Speed and GPS.
2. Warning Vehicle Information which consist of: Gas, Gear, Oil and Mileage.
3. Navigation System which consist of: Current Direction, Distance and Next Direction.


### Requirements: configuration

This part will need to be refactored and the configuration values
must be from a configuration file or program argument. For now, the
following needs to be updated.

1. can_main.py
- __FAKE_CAN_LOC: Add your computers full path to the projects /data/fakecandata.csv
- __VEHICLE_INFO_URL: Add ip and port of the Flask server on your computer (This may not require a change)
- __NAV_INFO_URL: Add ip and port of the Flask server on your computer (This may not require a change)

2. nav_main.py -
- __FAKE_NAV_LOC: Add your computers full path to the projects /data/fakenavndata.csv
- __NAV_INFO_URL: Add ip and port of the Flask server on your computer (This may not require a change)


### Requirements: software

1. Python packages from requirements.txt.
   It can be access through pip install -r requirements.txt


### Requirements: hardware

N/A

### Design: General Design

There are 3 explicit threads created. They are the following:

1. can_main.py: for simulated CAN bus processing
2. nav_main.py: for simulated Navigation system data processing
3. eld_service.py: for hosting the REST services
