

class Tire(object):

    def __is_flat(self) -> bool:
        return self.__is_flat

    def __set_is_flat(self, is_flat: bool):
        self.__is_flat = is_flat

    is_flat = property(__is_flat, __set_is_flat)



