from serial.can.data.gps import GPS


class FakeGeneralData(object):

    def __get_current_speed(self) -> float:
        return self.__current_speed

    def __set_current_speed(self, current_speed: float):
        self.__current_speed = current_speed

    def __get_current_gps(self) -> GPS:
        return self.__gps

    def __set_current_gps(self, gps: GPS):
        self.__gps = gps

    current_speed = property(__get_current_speed, __set_current_speed)
    current_gps = property(__get_current_gps, __set_current_gps)
