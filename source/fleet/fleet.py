from math import sqrt, ceil
from typing import List

from source.ships.vessel import Vessel


class Fleet(object):
    ships = List[Vessel]

    def __init__(self):
        self.name = ""
        self.owner = None
        self.location = None
        self.ships = []

    @property
    def signal_linear(self) -> int:
        return sum([x.signal for x in self.ships])

    @property
    def signal_sqrt(self):
        return ceil(sqrt(self.signal_linear))

    def fight(self):
        for ship in self.ships:
            ship.fight()

    def cleanup(self):
        self.ships = list(filter(lambda x: not x.is_dead, self.ships))
