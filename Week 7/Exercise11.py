"""Exercise 11 from Chapter 7 of our textbook."""


# magic_square = [
#     [4,9,2],
#     [3,5,7],
#     [8,1,6]
# ]


square_display_text = """\
[{0}, {1}, {2}],
[{3}, {4}, {5}],
[{6}, {7}, {8}]
"""

def format_square_display_text(args: list):
    """Format the square display with the user's arguments."""
    # Add an 'x' to indicate where the user's
    #   next input will go.
    if len(args) < 9:
        args.append('x')
    
    # Fill blank values with spaces
    while len(args) < 9:
        args.append(' ')
        
    return square_display_text.format(*args)


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
            # Send a copy of the list so we don't
            #   mutate user_inputs within the format function.
            print(format_square_display_text(user_inputs[:]))
            
            while True:
                try:
                    number = int(input("> "))
                except ValueError:
                    print("Error: Input was not a number.\n")
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
    print('\n' + format_square_display_text(user_inputs[:]))
    if a_value_not_equal:
        print("Magic square sums not equal!")
    else:
        print("This is a magic square. All sums are equal! :)")