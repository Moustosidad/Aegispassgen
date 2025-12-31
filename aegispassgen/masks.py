import itertools
import string

SETS = {
    "?l": string.ascii_lowercase,
    "?u": string.ascii_uppercase,
    "?d": string.digits,
    "?s": "!@#$%^&*"
}


def parse_mask(mask):
    tokens = []
    i = 0
    while i < len(mask):
        token = mask[i:i+2]
        if token in SETS:
            tokens.append(SETS[token])
            i += 2
        else:
            tokens.append(mask[i])
            i += 1
    return tokens


def generate_mask(mask, limit):
    pools = parse_mask(mask)
    produced = 0

    for combo in itertools.product(*pools):
        yield "".join(combo)
        produced += 1
        if produced >= limit:
            return
