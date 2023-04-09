from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 200
    started = False
    fuel = 80
    fuel_consumption = 15

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if Vehicle.started is not True:
            if self.fuel > 0:
                Vehicle.started = True
            else:
                raise LowFuelError('Нет топлива!')


    def move(self):
        if self.fuel_consumption / 100 * self.weight <= self.fuel and Vehicle.started:
            self.fuel = self.fuel_consumption / 100 * self.weight
        else:
            raise NotEnoughFuel('Топлива не хватит!')

