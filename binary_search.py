def binary_search(array, target):
    """
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    returns:
      boolean: whether or not the target is in the array
    """

    if len(array) == 1:
        return array[0] == target
    elif len(array) == 0:
        return False

    idx = len(array) // 2

    while len(array) > 1:
        if array[idx] == target:
            return True
        elif array[idx] < target:
            array = array[idx:]
            idx = len(array) // 2
        elif array[idx] > target:
            array = array[:idx]
            idx = len(array) // 2
    return False


def recursive_binary_search(array, target, start_index, end_index):
    """
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """
    idx = start_index + int((end_index - start_index) / 2)

    if array[idx] == target:
        return idx
    elif start_index == end_index:
        return -1
    elif target > array[idx]:
        start_index = idx + 1
    elif target < array[idx]:
        end_index = idx

    return recursive_binary_search(array, target, start_index, end_index)


found = recursive_binary_search([1, 2, 3, 4, 5, 6], 6, 0, 5)
print("Pass" if found == 5 else "Fail")

found = binary_search([1, 2, 3, 4, 5, 7], 6)
print("Pass" if not found else "Fail")

found = binary_search([1, 2, 3, 4, 5, 6, 7], 6)
print("Pass" if found else "Fail")

found = binary_search([1, 2, 3, 4, 5, 8, 7], 6)
print("Pass" if not found else "Fail")

found = binary_search(list(range(0, 100000)), 99999)
print("Pass" if found else "Fail")

found = binary_search(list(range(100000)), 100000)
print("Pass" if not found else "Fail")
