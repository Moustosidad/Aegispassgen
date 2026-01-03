import itertools


class Combinator:
    def __init__(self, words, random):
        self.words = words[:]
        random.shuffle(self.words)

    def stream(self):
        # 1 palabra
        for w in self.words:
            yield [w]

        # 2 palabras cruzadas
        for c in itertools.permutations(self.words, 2):
            yield list(c)

        # 3 palabras cruzadas
        if len(self.words) >= 3:
            for c in itertools.permutations(self.words, 3):
                yield list(c)
