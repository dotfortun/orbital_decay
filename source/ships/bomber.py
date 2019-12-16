#  Copyright (c) Shane Bell 2019

from source.ships.vessel import Vessel


class Bomber(Vessel):
    def __init__(self):
        super(Bomber, self).__init__()
        self.max_hp = 2
        self.hp = 0
        self.armor = 1
        self.damage = 4
