from serial.can.data.gps import GPS


class FakeGeneralData(object):

    def __init__(self, speed: float, gps: GPS):
        self.__speed = speed
        self.__gps = gps

    @property
    def speed(self) -> float:
        return self.__speed

    @property
    def gps(self) -> GPS:
        return self.__gps

    def get_json(self):
        return {
            'speed': str(self.speed),
            'gps': {
                'time': str(self.gps.time),
                'latitude': str(self.gps.latitude),
                'longitude': str(self.gps.longitude),
                'fix_quality': str(self.gps.fix_quality),
                'altitude': str(self.gps.altitude),
                'height': str(self.gps.height)
            }
        }
