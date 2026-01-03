class Mutator:
    def __init__(self, numbers, random):
        self.numbers = numbers
        self.random = random

    def apply(self, parts):
        base = "".join(parts)

        yield base.lower()
        yield base.capitalize()

        # separadores humanos
        yield "_".join(parts)
        yield ".".join(parts)

        # palabra + numero
        for n in self.numbers:
            yield f"{base}{n}"
            yield f"{parts[0]}{n}{parts[-1]}"

        # iniciales + numero
        initials = "".join(p[0] for p in parts)
        for n in self.numbers:
            yield f"{initials}{n}"
