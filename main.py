#  Copyright (c) Shane Bell 2019

from source.fleet.fleet import Fleet
from source.grid.grid import Grid

red = Fleet()
red.name = "Red"
blu = Fleet()
blu.name = "Blu"

battlefield = Grid(red, blu)
