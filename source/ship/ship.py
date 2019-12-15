#  Copyright (c) Shane Bell 2019

from collections import namedtuple
from math import sqrt
from typing import Type


class Vessel(object):
    def __init__(self):
        self.max_hp = 1
        self.hp = int(self.max_hp)
        self.armor = 0
        self.speed = 2
        self.range = 1
        self.damage = 1
        self.size = namedtuple('Size', ['x', 'y'])
        self.pos = namedtuple('Position', ['x', 'y'])
        self.signal = 1
        self.has_acted = False
        self.targeted = None

    def target(self, other: Type[Vessel]):
        self.targeted = other

    @property
    def has_targeted(self):
        return self.targeted is not None

    def fight(self):
        self.targeted.hp -= max([self.damage - other.armor - (self.distance(other) - self.range), 0])
        self.targeted = None
        self.has_acted = True

    def distance(self, other):
        return sqrt(
            ((self.pos.x - other.pos.x) ** 2) + ((self.pos.y - other.posy) ** 2)
        )

    def move(self, x, y):
        self.pos = x, y

    @property
    def is_dead(self):
        return self.hp <= 0
