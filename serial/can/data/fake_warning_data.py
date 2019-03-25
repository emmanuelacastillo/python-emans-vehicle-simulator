from serial.can.data.tire import Tire


class FakeWarningData(object):

    def __init__(self, gas_level: int, gear: str, mileage: int, oil: int,
                 tire_1: int, tire_2: int, tire_3: int, tire_4: int):
        self.__gas_level = gas_level
        self.__gear = gear
        self.__mileage = mileage
        self.__oil = oil
        self.__tires = []
        self.__tires.append(Tire(True if tire_1 == 0 else False))
        self.__tires.append(Tire(True if tire_2 == 0 else False))
        self.__tires.append(Tire(True if tire_3 == 0 else False))
        self.__tires.append(Tire(True if tire_4 == 0 else False))

    @property
    def gas_level(self):
        return self.__gas_level

    @property
    def gear(self):
        return self.__gear

    @property
    def mileage(self):
        return self.__mileage

    @property
    def oil(self):
        return self.__oil

    @property
    def tires(self):
        return self.__tires

    def get_json(self):
        return {
            'gas_level': str(self.gas_level),
            'gear': str(self.gear),
            'mileage': str(self.mileage),
            'oil': str(self.oil),
            'tire_1': {
                'is_flat': str(self.tires[0].is_flat)
            },
            'tire_2': {
                'is_flat': str(self.tires[1].is_flat)
            },
            'tire_3': {
                'is_flat': str(self.tires[2].is_flat)
            },
            'tire_4': {
                'is_flat': str(self.tires[3].is_flat)
            },
        }
