"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: int
    pistons: int

    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons







