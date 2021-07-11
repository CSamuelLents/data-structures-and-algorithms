"""
Given an array of length = n containing integers from 0 to n - 2, with each number appearing in the array
exactly once, except for a single duplicate, find and return the duplicate number

The time complexity for this problem is O(n), and the space-complexity is O(1).
"""
import functools


def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    arg_sum = functools.reduce(lambda a, n: a+n, arr)
    deduped_sum = functools.reduce(lambda a, n: a+n, range(len(arr) - 1))

    return arg_sum - deduped_sum


print(duplicate_number([1, 0, 0, 2]))
