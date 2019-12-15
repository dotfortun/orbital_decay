#  Copyright (c) Shane Bell 2019

from math import sqrt


class Vessel(object):
    def __init__(self):
        self.max_hp = 1
        self.hp = int(self.max_hp)
        self.armor = 0
        self.speed = 2
        self.range = 1
        self.damage = 1
        self.size = 1, 1
        self.pos = 0, 0
        self.has_acted = False

    def fight(self, other):
        other.hp -= int(max([self.damage - other.armor - self.distance(other), 0]))
        self.has_acted = True

    def distance(self, other):
        return sqrt(
            ((self.pos[0] - other.pos[0]) ** 2) + ((self.pos[1] - other.pos[1]) ** 2)
        )

    def move(self, x, y):
        self.pos = x, y

    @property
    def is_dead(self):
        return self.hp <= 0
