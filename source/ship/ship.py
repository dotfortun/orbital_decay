class Vessel(object):
    def __init__(self):
        self.max_hp = 1
        self.hp = self.max_hp
        self.speed = 1
        self.range = 1
        self.damage = 1
        self.size = 1, 1
        self.pos = 0, 0
        self.has_moved = False

    def fight(self, other):
        other.hp -= self.damage
