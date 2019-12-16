#  Copyright (c) Shane Bell 2019
from typing import Type, List

from source.ships.vessel import Vessel


class Destroyer(Vessel):
    def __init__(self):
        super(Destroyer, self).__init__()
        self.armor = 1
        self.speed = 3
        self.damage = 2
        self.range = 3
        self.size.x = 1
        self.size.y = 2
        self.signal = 4
        self.targeted = List[Vessel]
        self.max_targets = 2

    def target(self, *others: Type[Vessel]):
        for idx, shp in enumerate(others):
            if idx >= self.max_targets:
                break
            self.targeted.append(shp)

    def fight(self):
        while len(self.targeted) > 0:
            target = self.targeted.pop()
            target.hp -= max([
                self.damage - target.armor - (
                        self.distance(target) - self.range
                ),
                0
            ])
        self.has_acted = True
