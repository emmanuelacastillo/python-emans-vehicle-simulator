import pandas as pd
from pandas import DataFrame
from serial.nav.hardware.nav_client import NavClient
from serial.nav.data.fake_navigation_data import FakeNavigationData


class NavClientFakeData(NavClient):
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

    def receive(self, data_index: int):
        read_data = self._data.iloc[data_index, :]
        nav_data = FakeNavigationData(read_data['current_direction'], read_data['distance'],
                                      read_data['next_direction'])
        return nav_data
