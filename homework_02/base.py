from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int
    started = False
    fuel: int
    fuel_consumption: int

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is not True:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Нет топлива!')


    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        if max_distance >= distance:
            self.fuel = self.fuel - self.fuel_consumption * distance

        else:
            raise NotEnoughFuel('Топлива не хватит!')


