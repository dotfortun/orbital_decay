#  Copyright (c) Shane Bell 2019

from unittest import TestCase
from source.ship.ship import Vessel


class TestVessel(TestCase):
    def setUp(self) -> None:
        self.blue = Vessel()
        self.red = Vessel()
        self.red.pos = 1, 0
        super().setUp()

    def test_fight(self):
        self.blue.fight(self.red)
        self.assertEqual(self.blue.hp, 1)
        self.assertEqual(self.red.hp, 1)
        self.assertFalse(self.blue.is_dead)
        self.assertFalse(self.red.is_dead)
        self.blue.move(1, 0)
        self.blue.fight(self.red)
        self.assertEqual(self.blue.hp, 1)
        self.assertEqual(self.red.hp, 0)
        self.assertFalse(self.blue.is_dead)
        self.assertTrue(self.red.is_dead)

    def test_distance(self):
        self.assertEqual(self.blue.distance(self.red), 1.0)
