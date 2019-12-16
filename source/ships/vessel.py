#  Copyright (c) Shane Bell 2019

from collections import namedtuple
from math import sqrt
import random


class Vessel(object):
    def __init__(self):
        self.max_hp = 1
        self.hp = int(self.max_hp)
        self.armor = 0
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
        self.dodge = 0

    def target(self, other):
        self.targeted = other

    @property
    def has_targeted(self):
        return self.targeted is not None

    def fight(self):
        if self.targeted is not None:
            if random.random() > self.targeted.dodge:
                self.targeted.hp -= max([
                    self.damage - self.targeted.armor - (
                            self.distance(self.targeted) - self.range
                    ),
                    0
                ])
            self.targeted = None
            self.has_acted = True

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
