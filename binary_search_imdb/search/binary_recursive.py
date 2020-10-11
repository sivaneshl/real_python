# Binary search - Recursive


def find_index(elements, value, key=lambda x: x):
    """ search elements by value and return the index """

    def recursive(left, right):
        if left <= right:
            # find the middle element
            middle = (left + right) // 2
            middle_element = key(elements[middle])
            # if the middle element is the search element...
            if middle_element == value:
                return middle
            # find which half to search
            if middle_element < value:
                return recursive(middle+1, right)
            elif middle_element > value:
                return recursive(left, middle-1)
        return None
    return recursive(0, len(elements)-1)


def find(elements, value, key=lambda x: x):
    """ find the element from elements and return the element """
    index = find_index(elements, value, key)
    return None if index is None else elements[index]


def contains(elements, value, key=lambda x: x):
    """ checks if the value is in the elements """
    return find_index(elements, value, key) is not None

