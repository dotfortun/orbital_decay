#  Copyright (c) Shane Bell 2019

from source.ships.vessel import Vessel


class Fighter(Vessel):
    def __init__(self, pos=(0, 0)):
        super(Fighter, self).__init__()
        self.pos.x = pos[0]
        self.pos.y = pos[1]
        self.speed = 5
