"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import LowFuelError


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self):
        pass

    def remove_all_cargo(self):
        cargonull = self.cargo
        self.cargo = 0
        return cargonull
