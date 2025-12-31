import itertools

SEPARATORS = ["", "_", ".", "-", "@", "!"]

LEET_MAP = str.maketrans({
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "5"
})


def case_variants(word):
    yield word.lower()
    yield word.upper()
    yield word.capitalize()
    if len(word) > 1:
        yield word[0].upper() + word[1:].lower()


def leet_variants(word):
    yield word
    yield word.translate(LEET_MAP)


def stretch_variants(word):
    yield word
    if len(word) > 2:
        yield word + word[-1]
        yield word * 2


def base_mutations(word):
    for c in case_variants(word):
        for l in leet_variants(c):
            for s in stretch_variants(l):
                yield s


def combine_with_numbers(word, numbers):
    if not numbers:
        yield word
        return

    for n in numbers:
        for sep in SEPARATORS:
            yield f"{word}{sep}{n}"
            yield f"{n}{sep}{word}"
            if len(word) > 3:
                mid = len(word) // 2
                yield f"{word[:mid]}{n}{word[mid:]}"