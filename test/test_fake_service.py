import unittest
import datetime
from services.fake_service import FakeGpsData
from serial.can.data.gps import GPS


class TestFakeGpsData(unittest.TestCase):
    __FAKE_GPS_LOC: str = 'C:\\Users\\emman\\Desktop\\projects\\python-emans-vehicle-simulator\\data\\fakegpsdata.csv'

    def test_constructor_exception(self):
        with self.assertRaises(FileNotFoundError):
            FakeGpsData('fake_file')

    def test_constructor_one_instance(self):
        fake_data_1: FakeGpsData = FakeGpsData(self.__FAKE_GPS_LOC)
        fake_data_2: FakeGpsData = FakeGpsData(self.__FAKE_GPS_LOC)
        self.assertTrue(fake_data_1 is fake_data_2)

    def test_read_value_valid_value(self):
        gps_value: GPS = FakeGpsData(self.__FAKE_GPS_LOC).read_value(0)
        self.assertEqual(gps_value.time, datetime.time, 'invalid time')
        self.assertEqual(gps_value.latitude, 32.715738, 'invalid latitude')
        self.assertEqual(gps_value.longitude, -117.1610838, 'invalid longitude')
        self.assertEqual(gps_value.fix_quality, 8, 'invalid fix quality')
        self.assertEqual(gps_value.altitude, 545.4, 'invalid altitude')
        self.assertEqual(gps_value.height, 46.9, 'invalid height')

