

class Tire(object):

    def __init__(self, is_flat: bool):
        self.__is_flat = is_flat

    @property
    def is_flat(self):
        return self.__is_flat



