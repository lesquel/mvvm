class Contacto:
    def __init__(self, name: str, last_name: str, phone_number: int, gender: str):
        self._name = name
        self._last_name = last_name
        self._phone_number = phone_number
        self._gender = gender

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number: int):
        self._phone_number = phone_number

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def name(self, gender: str):
        self._gender = gender
