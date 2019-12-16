#  Copyright (c) Shane Bell 2019

from source.ships.vessel import Vessel


class SubcapitalShip(Vessel):
    def __init__(self):
        super(Vessel, self).__init__()
        self.dodge = 1/10
