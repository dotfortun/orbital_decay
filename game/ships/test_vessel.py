from unittest import TestCase
from game.ships.vessel import Vessel


class TestVessel(TestCase):
    def setUp(self) -> None:
        self.blue = Vessel()
        self.red = Vessel()
        self.red.pos.x = 1
        self.red.pos.y = 0

    def test_fight(self):
        self.blue.target(self.red)
        self.blue.fight()
        self.assertEqual(self.blue.hp, 1)
        self.assertEqual(self.red.hp, 0)
        self.assertFalse(self.blue.is_dead)
        self.assertTrue(self.red.is_dead)

    def test_distance(self):
        self.assertEqual(self.blue.distance(self.red), 1.0)
