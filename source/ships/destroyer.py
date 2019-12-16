#  Copyright (c) Shane Bell 2019
from typing import Type, List

from source.ships.capital_ship import CapitalShip
from source.ships.vessel import Vessel


class Destroyer(CapitalShip):
    def __init__(self):
        super(Destroyer, self).__init__()
        self.armor = 2
        self.max_hp = 4
        self.hp = 4
        self.speed = 3
        self.damage = 2
        self.range = 3
        self.size.x = 1
        self.size.y = 2
        self.signal = 4
        self.targeted = List[Vessel]
        self.max_targets = 2
