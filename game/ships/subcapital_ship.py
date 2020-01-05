from game.ships.vessel import Vessel


class SubcapitalShip(Vessel):
    def __init__(self):
        super().__init__()
        self.dodge = 1/10
