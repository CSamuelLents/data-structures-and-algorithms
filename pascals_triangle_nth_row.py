"""
inputs:
  Number corresponding to the row of Pascal's Triangle
output:
  An ordered array containing the integers comprising the row of Pascal's Triangle denoted by the input
"""


def nth_row_pascal(n):
    if type(n) != int or n < 0:
        raise TypeError('Parameter must be an integer greater than 0')

    if n < 2:
        return [1] * (n + 1)

    row = [1, 2, 1]

    while len(row) <= n:
        row = get_next_row(row)

    return row


def get_next_row(row):
    next_row = [1]

    for i in range(1, len(row)):
        next_row.append(row[i] + row[i - 1])

    next_row.append(1)
    return next_row


print(nth_row_pascal(0))
print(nth_row_pascal(1))
print(nth_row_pascal(2))
print(nth_row_pascal(3))
print(nth_row_pascal(10))
