

class FakeNavigationData(object):

    def __init__(self, current_direction: str, distance: float, next_direction: str):
        self.__current_direction: str = current_direction
        self.__distance: str = distance
        self.__next_direction: str = next_direction
    
    @property
    def current_direction(self):
        return self.__current_direction

    @property
    def distance(self):
        return self.__distance

    @property
    def next_direction(self):
        return self.__next_direction

    def get_json(self):
        return {
            'current_direction': str(self.current_direction),
            'distance': str(self.distance),
            'next_direction': str(self.next_direction),
        }
