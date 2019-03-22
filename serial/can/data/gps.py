import datetime


class GPS(object):

    def __init__(self):
        self.time: datetime
        self.latitude: float
        self.longitude: float
        self.fix_quality: int
        self.altitude: float
        self.height: float

    @property
    def time(self) -> datetime:
        return self.__time

    @time.setter
    def time(self, time: datetime):
        self.__time = time

    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self.__latitude = latitude

    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self.__longitude = longitude

    @property
    def fix_quality(self) -> int:
        return self.__fix_quality

    @fix_quality.setter
    def fix_quality(self, fix_quality: float):
        self.__fix_quality = fix_quality

    @property
    def altitude(self) -> float:
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude: float):
        self.__altitude = altitude

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height