from random import randint


class Dice:

    def __init__(self):
        self.result = None
        self.roll()

    def roll(self):
        self.result = randint(1, 6)

    def check(self):
        return self.result

