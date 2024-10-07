"""Exercise 11 from Chapter 7 of our textbook."""

from string import Formatter

# magic_square = [
#     [4,9,2],
#     [3,5,7],
#     [8,1,6]
# ]

class UnseenFormatter(Formatter):
    """Custom formatter to replace string.format().
    Allows us to use default values if a value doesn't exist."""
    def get_value(self, key, args, kwds):
        if isinstance(key, str):
            try:
                return kwds[key]
            except KeyError:
                return key
        else:
            return Formatter.get_value(key, args, kwds)


fmt = UnseenFormatter()
square_display = """\
[{ }, { }, { }],
[{ }, { }, { }],
[{ }, { }, { }]
"""


if __name__ == "__main__":
    print("\nWelcome to the Lo Schu Magic Square validator.")
    
    user_inputs = []
    
    magic_square = [
        [],
        [],
        [],
    ]
    
    print("Enter numbers starting from top left to right of the diagram:")
    
    # Take in magic square
    for row in range(3):
        for col in range(3):
            
            try:
                user_inputs.remove('x')
            except ValueError:
                pass
            
            if len(user_inputs) != 9:
                user_inputs.append('x')
            
            # now to fix the display:
            print(fmt.format(square_display, user_inputs))
            
            while True:
                try:
                    number = int(input("> "))
                except ValueError:
                    print("Error: Input was not a number.")
                else:
                    user_inputs.append(number)
                    magic_square[row].append(number)
                    break

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