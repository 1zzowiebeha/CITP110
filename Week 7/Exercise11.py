"""Exercise 11 from Chapter 7 of our textbook."""

import numpy

magic_square = [
    [7,8,9],
    [4,5,6],
    [1,2,3]
]

row_sums = [sum(row) for row in magic_square]

col_sums = []
for column in range(3):
    column_sum = 0
    for row in magic_square:
        column_sum += row[column]

diagonal_sum = 0
diagonal_sum += magic_square[0][0]
diagonal_sum += magic_square[1][1]
diagonal_sum += magic_square[2][2]

# complete later on meh