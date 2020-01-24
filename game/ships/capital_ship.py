import random
from typing import Type

from game.ships.vessel import Vessel


class CapitalShip(Vessel):
    def __init__(self):
        super().__init__()
        self.max_targets = 1
        self.armor = 0

    def target(self, *others: Type[Vessel]):
        for idx, shp in enumerate(others):
            if idx >= self.max_targets:
                break
            self.targeted.append(shp)

    def defend(self, dmg: int):
        self.hp -= max([
            dmg - self.armor,
            0
        ])
