from game.ships.vessel import Vessel


class Cruiser(Vessel):
    def __init__(self):
        super(Cruiser, self).__init__()
        self.max_hp = 8
        self.hp = 8
        self.armor = 2
        self.damage = 4
        self.range = 8
