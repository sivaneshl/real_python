# Binary Search - Iterative method

def find_index(elements, value, key=lambda x:x):
    """ search elements by value and retutn the index """

    # setting the upper bound and lower bound
    left, right = 0, len(elements) - 1

    while left <= right:
        # find the middle element - use integer division
        middle = (left + right) // 2

        # if the middle element is the search element...
        middle_element = key(elements[middle])
        if middle_element == value:
            return middle

        # find which half to search
        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1


def find(elements, value, key=lambda x: x):
    """ find the element from elements and return the element """
    index = find_index(elements, value, key)
    return None if index is None else elements[index]


def contains(elements, value, key=lambda x: x):
    """ checks if the value is in the elements """
    return find_index(elements, value, key) is not None


def find_leftmost_index(elements, value, key=lambda x: x):
    """ mimic the bisect_left() functionality and return the index from the left if there are duplicates """
    # before finding the leftmost instance of a duplicate element, we need to determine if there is such element at all
    index = find_index(elements, value, key)
    if index is not None:
        # if some index is found, then we can keep moving left until we come across an element with a different key or
        # there are no elements at all
        while index >= 0 and key(elements[index]) == value:
            index -= 1
        # once we go past the leftmost element, we need to move the index back by one position to right
        index += 1
    return index


def find_rightmost_index(elements, value, key=lambda x: x):
    """ mimic the bisect_right() functionality and return the index from the right if there are duplicates """
    # before finding the rightmost instance of a duplicate element, we need to determine if there is such element at all
    index = find_index(elements, value, key)
    if index is not None:
        # if some index is found, then we can keep moving right until we come across an element with a different key or
        # there are no elements at all
        while index < len(elements) and key(elements[index]) == value:
            index += 1
        # once we go past the rightmost element, we need to move the index back by one position to the left
        index -= 1
    return index


def find_all_indices(elements, value, key=lambda x: x):
    """ returns all the indices of the given element from elements """
    left = find_leftmost_index(elements, value, key)
    right = find_rightmost_index(elements, value, key)
    if left and right:
        return set(range(left, right+1))
    return set()


def find_leftmost(elements, value, key=lambda x: x):
    """ returns the element in elements from the leftmost index """
    index = find_leftmost_index(elements, value, key)
    return None if index is None else elements[index]


def find_rightmost(elements, value, key=lambda x: x):
    """ returns the element in elements from the rightmost index """
    index = find_rightmost_index(elements, value, key)
    return None if index is None else elements[index]


def find_all(elements, value, key=lambda x: x):
    """ returns all elements from the all the matching indices """
    return {elements[i] for i in find_all_indices(elements, value, key)}
