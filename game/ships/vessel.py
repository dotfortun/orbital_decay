from collections import namedtuple
from math import sqrt
import random


class Vessel(object):
    max_hp = 1
    hp = int(max_hp)
    armor = 0
    speed = 1
    range = 1
    damage = 1
    size = namedtuple('Size', ['x', 'y'])
    size.x = 1
    size.y = 1
    pos = namedtuple('Position', ['x', 'y'])
    pos.x = 1
    pos.y = 1
    signal = 1
    has_acted = False
    targeted = None
    dodge = 0

    def __init__(self):
        self.max_hp = 1
        self.hp = int(self.max_hp)
        self.speed = 1
        self.range = 1
        self.damage = 1
        self.size = namedtuple('Size', ['x', 'y'])
        self.size.x = 1
        self.size.y = 1
        self.pos = namedtuple('Position', ['x', 'y'])
        self.pos.x = 1
        self.pos.y = 1
        self.signal = 1
        self.has_acted = False
        self.targeted = None

    def target(self, other):
        self.targeted = other

    @property
    def has_targeted(self):
        return self.targeted is not None

    def distance(self, other):
        return sqrt(
            ((self.pos.x - other.pos.x) ** 2) + ((self.pos.y - other.pos.y) ** 2)
        )

    def move(self, x: int, y: int):
        self.pos.x = x
        self.pos.y = y

    @property
    def is_dead(self):
        return self.hp <= 0

    def attack(self, other):
        other.defend(max([
            self.damage - (
                self.distance(other) - self.range
            ),
            0
        ]))

    def defend(self, dmg: int):
        self.hp -= dmg
