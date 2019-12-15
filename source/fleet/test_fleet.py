#  Copyright (c) Shane Bell 2019

from unittest import TestCase
from source.fleet.fleet import Fleet
from source.ship.ship import Vessel


class TestFleet(TestCase):
    def setUp(self) -> None:
        self.blue = Fleet()
        self.red = Fleet
        self.blue.name = "Blue"
        self.blue.ships = [
            Vessel()
        ] * 10
        self.red.name = "Red"
        self.red.ships = [
            Vessel
        ] * 10

    def test_signal_linear(self):
        self.assertEqual(self.blue.signal_linear, 10)

    def test_signal_sqrt(self):
        self.assertEqual(self.blue.signal_sqrt, 4)
