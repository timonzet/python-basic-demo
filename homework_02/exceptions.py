"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, texterror):
        self.text = texterror


class CargoOverload(LowFuelError):
    pass


class NotEnoughFuel(LowFuelError):
    pass


