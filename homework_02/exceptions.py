"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
from homework_02.base import Vehicle


class LowFuelError(Exception):
    def __init__(self, texterror):
        self.text = texterror


class CargoOverload(LowFuelError):
    pass


class NotEnoughFuel(LowFuelError):
    pass


