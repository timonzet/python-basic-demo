"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, max_cargo, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, num):
        if Plane.cargo + num <= Plane.max_cargo:
            Plane.cargo += num
        else:
            raise CargoOverload("Перегруз")

    def remove_all_cargo(self):
        cargonull = self.cargo
        self.cargo = 0
        return cargonull
