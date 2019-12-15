#  Copyright (c) Shane Bell 2019
from math import sqrt, ceil
from typing import List

from source.ship.ship import Vessel


class Fleet(object):
    def __init__(self):
        self.name = ""
        self.owner = None
        self.location = None
        self.ships = List[Vessel]

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
