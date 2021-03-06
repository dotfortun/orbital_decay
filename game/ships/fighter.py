from game.ships.subcapital_ship import SubcapitalShip


class Fighter(SubcapitalShip):
    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.name = "f"
        self.pos.x = pos[0]
        self.pos.y = pos[1]
        self.speed = 5
        self.max_hp = 2
        self.hp = 2
        self.dodge = 2/10
