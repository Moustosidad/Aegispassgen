import argparse


class Config:
    def __init__(self, words, numbers, max_results, seed, ui):
        self.words = words
        self.numbers = numbers
        self.max_results = max_results
        self.seed = seed
        self.ui = ui

    @staticmethod
    def from_args():
        p = argparse.ArgumentParser("AegisPassGen")
        p.add_argument("-w", "--words", nargs="+", required=True)
        p.add_argument("-n", "--numbers", nargs="+", default=[])
        p.add_argument("-m", "--max", type=int, default=100_000)
        p.add_argument("--seed", type=int)
        p.add_argument("--ui", action="store_true")
        a = p.parse_args()

        return Config(a.words, a.numbers, a.max, a.seed, a.ui)
