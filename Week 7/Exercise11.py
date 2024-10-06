"""Exercise 11 from Chapter 7 of our textbook."""

magic_square = [
    [7,8,9],
    [4,5,6],
    [1,2,3]
]

# Take in magic square
# ...

# Sum all rows, columns, and the diagonal
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

# Check equality
a_value_not_equal = False
for sum in row_sums:
    if sum != diagonal_sum:
        a_value_not_equal = True
        
for sum in col_sums:
    if sum != diagonal_sum:
        a_value_not_equal = True

# Output
if a_value_not_equal:
    print("Magic square sums not equal!")
else:
    print("This is a magic square. All sums are equal! :)")