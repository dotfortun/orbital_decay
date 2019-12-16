#  Copyright (c) Shane Bell 2019

from collections import namedtuple
from typing import Type

from source.fleet.fleet import Fleet


class Grid(object):
    def __init__(self, red: Type[Fleet], blue: Type[Fleet]):
        self.red = red
        self.blue = blue
        self.size = namedtuple('Size', ['x', 'y'])
        self.size.x = 10
        self.size.y = 10
        for ship in self.red.ships:
            ship.pos.x = self.size.x - ship.pos.x
            ship.pos.y = self.size.y - ship.pos.y
