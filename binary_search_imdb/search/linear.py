def find_index(elements, value, key=lambda x: x):
    """ retuns the index of the matching element in the elements """
    for i, element in enumerate(elements):
        if key(element) == value:
            return i
    return None


def find(elements, value, key=lambda x: x):
    """ returns the element if present in elements """
    index = find_index(elements, value, key)
    return None if index is None else elements[index]


def contains(elements, value, key=lambda x: x):
    """ returns true if the element is present in elements """
    return find_index(elements, value, key) is not None
