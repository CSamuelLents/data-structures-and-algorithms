"""
Given a list of numbers, find the first and last indices of a given search term
using binary search.
"""

def first_and_last_index(arr, number):
    first_index = get_term_position(arr, number, 0, len(arr) - 1, "first")
    last_index = get_term_position(arr, number, 0, len(arr) - 1, "last")

    return [first_index, last_index]


def get_term_position(arr, number, start_index, end_index, position):
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index) // 2

    if arr[mid_index] == number:
        if position == "first":
            args = [arr, number, start_index, mid_index - 1]
        elif position == "last":
            args = [arr, number, mid_index + 1, end_index]

        curr_pos = get_term_position(*args, position)

        if curr_pos != -1:
            search_result = curr_pos
        else:
            search_result = mid_index

        return search_result
    elif arr[mid_index] < number:
        return get_term_position(arr, number, mid_index + 1, end_index, position)
    else:
        return get_term_position(arr, number, start_index, mid_index - 1, position)


def test_function(test_case):
    input_list, number, solution = test_case
    output = first_and_last_index(input_list, number)

    print("Pass" if output == solution else "Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)
