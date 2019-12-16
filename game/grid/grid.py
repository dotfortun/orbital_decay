from collections import namedtuple
from itertools import islice
from typing import Type

from game.fleet.fleet import Fleet


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

    def __repr__(self):
        def chunk(it, size):
            return iter(lambda: tuple(islice(iter(it), size)), ())
        rep = ["."] * self.size.x * self.size.y
        for ship in self.red.ships + self.blue.ships:
            rep[ship.pos.x * self.size.x + ship.pos.y] = ship.name
        return '\n'.join([''.join(x) for x in chunk(rep, self.size.y)])
