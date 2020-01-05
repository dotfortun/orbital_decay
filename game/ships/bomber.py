from game.ships.subcapital_ship import SubcapitalShip


class Bomber(SubcapitalShip):
    def __init__(self):
        super().__init__()
        self.name = "b"
        self.max_hp = 2
        self.hp = 0
        self.armor = 1
        self.damage = 4
        self.dodge = 1/10
