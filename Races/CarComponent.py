# CarComponent.py
class CarComponent():
    _name: str

    def get_name(self):
        return self._name

class Engine(CarComponent):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def get_power(self):
        return self._power
