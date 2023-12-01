from itertools import permutations


def possible_permutations(args: list):
    for ch in list(permutations(args)):
        yield list(ch)