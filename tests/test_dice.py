import unittest
from src.dice import Dice


class TestDice(unittest.TestCase):
    def test_dice__next_returns_int(self):
        d = Dice()
        d.roll()
        self.assertTrue(0 < d.check() < 7)

    def test_dice_created(self):
        d = Dice()
        self.assertIsInstance(d, Dice)

    def test_dice_created_has_value(self):
        d = Dice()
        self.assertTrue(0 < d.check() < 7)


