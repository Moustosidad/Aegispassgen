import random
from .rules import base_mutations, combine_with_numbers


def generate(words, limit, randomize=False, seed=None, block_size=5000):
    if seed is not None:
        random.seed(seed)

    words = [w.strip() for w in words if w.strip()]
    numbers = [w for w in words if w.isdigit()]
    texts = [w for w in words if not w.isdigit()]

    produced = 0
    buffer = []

    for word in texts:
        for mutation in base_mutations(word):
            for candidate in combine_with_numbers(mutation, numbers):
                buffer.append(candidate)

                if len(buffer) >= block_size:
                    if randomize:
                        random.shuffle(buffer)

                    for item in buffer:
                        yield item
                        produced += 1
                        if produced >= limit:
                            return

                    buffer.clear()

    if randomize:
        random.shuffle(buffer)

    for item in buffer:
        yield item
        produced += 1
        if produced >= limit:
            return
