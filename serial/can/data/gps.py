import datetime


class GPS(object):

    def __init__(self, time: datetime, latitude: float, longitude: float,
                 fix_quality: int, altitude : float, height: float):
        self.__time: datetime = time
        self.__latitude: float = latitude
        self.__longitude: float = longitude
        self.__fix_quality: int = fix_quality
        self.__altitude: float = altitude
        self.__height: float = height

    @property
    def time(self) -> datetime:
        return self.__time

    @property
    def latitude(self) -> float:
        return self.__latitude

    @property
    def longitude(self) -> float:
        return self.__longitude

    @property
    def fix_quality(self) -> int:
        return self.__fix_quality

    @property
    def altitude(self) -> float:
        return self.__altitude

    @property
    def height(self) -> float:
        return self.__height
