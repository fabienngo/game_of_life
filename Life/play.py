from typing import Set, Tuple
from itertools import product
from copy import copy


def compute_neighbors(x: int, y: int)-> Set[Tuple]:
    """
    compute closest neighbors to a cell with integer coordinates x, y
    :param x:
    :param y:
    :return:
    """
    return {(x + i, y + j) for (i, j) in product({-1, 0, 1}, {-1, 0, 1}) if (i, j) != (0, 0)}


def compute_envelope(state: Set[Tuple]) -> Set[Tuple]:
    """
    compute the closest neighbors of a set of cells with integer coordinates. We call it the envelope of the set
    :param state:
    :return:
    """
    envelope = set(state)
    for x, y in state:
        envelope |= compute_neighbors(x, y)
    return envelope


def life(seed: Set[Tuple]):
    """
    implemetation of the Conway's game of life
    :param seed:
    :return:
    """
    old_state = seed.copy()
    new_state = set()
    while True:
        envelope = compute_envelope(old_state)
        for x, y in envelope:
            # the next line compute the numbers of neighbors that are alive
            n_living_neighbors = len(compute_neighbors(x, y).intersection(old_state))
            if (x, y) not in old_state:
                if n_living_neighbors == 3:
                    new_state.add((x, y))
            elif n_living_neighbors == 3 or n_living_neighbors == 2:
                new_state.add((x, y))
        old_state = copy(new_state)
        new_state = set()

if __name__ == "__main__":
    seed = {(0, 1), (1, 0), (0, -1), (-1, -1), (1, -1)}
    life(seed)




