import random


class RandomController:
    def __init__(self, seed=None):
        self.rand = random.Random(seed)

    def shuffle(self, seq):
        self.rand.shuffle(seq)
