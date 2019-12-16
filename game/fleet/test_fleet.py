from unittest import TestCase
from game.fleet.fleet import Fleet
from game.ships.vessel import Vessel


class TestFleet(TestCase):
    def setUp(self) -> None:
        self.blue = Fleet()
        self.red = Fleet()
        self.blue.name = "Blue"
        self.blue.ships = [
            Vessel()
        ] * 10
        self.red.name = "Red"
        self.red.ships = [
            Vessel()
        ] * 10

    def test_signal_linear(self):
        self.assertEqual(self.blue.signal_linear, 10)

    def test_signal_sqrt(self):
        self.assertEqual(self.blue.signal_sqrt, 4)

    def test_combat(self):
        for idx, shp in enumerate(self.red.ships):
            shp.target(self.blue.ships[idx])
            self.blue.ships[idx].target(shp)
        self.assertFalse(all([x.is_dead for x in self.blue.ships] + [x.is_dead for x in self.red.ships]))
        self.blue.fight()
        self.red.fight()
        self.assertEqual(len(self.blue.ships), 10)
        self.assertEqual(len(self.red.ships), 10)
        self.assertTrue(all([x.is_dead for x in self.blue.ships] + [x.is_dead for x in self.red.ships]))
        self.blue.cleanup()
        self.red.cleanup()
        self.assertEqual(len(self.blue.ships), 0)
        self.assertEqual(len(self.red.ships), 0)
