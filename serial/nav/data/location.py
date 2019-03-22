

class Location(object):
    
    def __get_address_num(self) -> int:
        return self.__address_num

    def __set_address_num(self, address_num: int):
        self.__address_num = address_num
        
    def __get_address_name(self) -> str:
        return self.__address_name

    def __set_address_name(self, address_name: str):
        self.__address_name = address_name
        
    def __get_address_2(self) -> str:
        return self.__address_2

    def __set_address_2(self, address_2: str):
        self.__address_2 = address_2
        
    def __get_city(self) -> str:
        return self.__city

    def __set_city(self, city: str):
        self.__city = city
    
    def __get_state(self) -> str:
        return self.__state

    def __set_state(self, state: str):
        self.__state = state
        
    def __get_zip_code(self) -> int:
        return self.__zip_code

    def __set_zip_code(self, zip_code: int):
        self.__zip_code = zip_code

    address_num = property(__get_address_num, __set_address_num)
    address_name = property(__get_address_name, __set_address_name)
    address_2 = property(__get_address_2, __set_address_2)
    city = property(__get_city, __set_city)
    state = property(__get_state, __set_state)
    zip_code = property(__get_zip_code, __set_zip_code)
