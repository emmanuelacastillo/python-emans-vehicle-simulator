import datetime
import pandas as pd
from pandas import DataFrame
from serial.can.data.gps import GPS
from serial.can.data.fake_general_data import FakeGeneralData
from serial.can.data.fake_warning_data import FakeWarningData
from serial.can.hardware.can_client import CanClient


class CanClientFakeData(CanClient):
    __FILE_NAME_IDX = 0
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            try:
                file_name = args[cls.__FILE_NAME_IDX]
                args = ()
                cls._instance = super().__new__(cls, *args, **kwargs)
                cls._data: DataFrame = pd.read_csv(file_name)
            except FileNotFoundError:
                cls._instance = None
                raise FileNotFoundError
            except OSError:  # file may be open
                cls._instance = None
                raise OSError
        return cls._instance

    @staticmethod
    def extract_general_data_general(read_data: DataFrame) -> FakeGeneralData:
        speed: float = read_data['speed']
        gps: GPS = GPS(datetime.datetime.now(), read_data['latitude'], read_data['longitude'], read_data['fix_quality'],
                       read_data['altitude'], read_data['height'])
        return FakeGeneralData(speed, gps)

    @staticmethod
    def extract_warning_data_general(read_data: DataFrame) -> FakeWarningData:
        return FakeWarningData(read_data['gas_level'], read_data['gear'], read_data['mileage'], read_data['oil'],
                               read_data['tire_1'], read_data['tire_2'], read_data['tire_3'], read_data['tire_4'])

    def receive(self, data_index: int):
        read_data = self._data.iloc[data_index, :]
        fake_general_data: FakeGeneralData = CanClientFakeData.extract_general_data_general(read_data)
        fake_warning_data: FakeWarningData = CanClientFakeData.extract_warning_data_general(read_data)
        return fake_general_data, fake_warning_data