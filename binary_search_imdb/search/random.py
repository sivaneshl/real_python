import random


def find_index(elements, value, key=lambda x: x):
    """ Returns the index of the matching element in elements """
    visited = set()
    while len(visited) < len(elements):
        random_index = random.randint(0, len(elements) - 1)
        visited.add(random_index)
        if key(elements[random_index]) == value:
            return random_index
    return None


def find(elements, value, key=lambda x: x):
    """ Returns the matching element from elements """
    index = find_index(elements, value, key)
    return None if index is None else elements[index]


def contains(elements, value, key=lambda x: x):
    """ Returns True if the value is present in elements """
    return find_index(elements, value, key) is not None