# Car.py
from CarComponent import Engine
from math import pi

class Car():
    def __init__(self, maker, model, year):
        self._maker = maker
        self._model = model
        self._year = year

    def add_component_to_car(self, **components):
        components_keys = components.keys()
        if "engine" in components_keys:
            self._engine = components["engine"]
        else:
            raise ValueError("No engines")
        self._speed = 2 * pi * 12 * self._engine.get_power()

    def get_speed(self):
        return self._speed

    def get_name(self):
        return f"{self._maker} {self._model} {self._year}"
