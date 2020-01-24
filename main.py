from flask import Flask

srv = Flask(__name__)

@srv.route('/')
def hello_world():
    return "Hello, world!"

# from game.fleet.fleet import Fleet
# from game.grid.grid import Grid
# from game.ships.bomber import Bomber
# from game.ships.destroyer import Destroyer
# from game.ships.fighter import Fighter
#
# from copy import deepcopy
#
# red = Fleet()
# red.name = "Red"
# blu = Fleet()
# blu.name = "Blu"
#
# red.ships.append(Destroyer())
# blu.ships = [
#     Fighter(),
#     Fighter(),
#     Bomber(),
#     Fighter(),
#     Fighter(),
#     Bomber(),
#     Fighter(),
#     Bomber(),
#     Fighter(),
#     Fighter()
# ]
#
# for idx, ship in enumerate(blu.ships):
#     ship.move(idx, 5)
# for ship in red.ships:
#     ship.move(5, 2)
#
# grid = Grid(red, blu)
# print(grid)
