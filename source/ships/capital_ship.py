#  Copyright (c) Shane Bell 2019

from source.ships.vessel import Vessel


class CapitalShip(Vessel):
    def __init__(self):
        super(CapitalShip, self).__init__()
        self.max_targets = 1

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
