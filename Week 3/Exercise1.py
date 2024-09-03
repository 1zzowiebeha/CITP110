"""Code for Exercise 1 from the textbook."""

###############
# Exercise 1: #
###############


try:
    number = int(input("Please enter a number:\n> "))
except ValueError:
    print("Error: The value you entered was not a number.")
else:
    print("\n* Information about your number:")
    if number < 0:
        print("The number is Negative.")
    elif number == 0:
        print("The number is Zero.")
    else:
        print("The number is Positive.")
    
    # Divide by two and check if the remainder is 0
    if number % 2 == 0:
        print("The number is Even.")
    # If a remainder exists, 2 can't perfectly fit into our number,
    # .. and so it is odd.
    else:
        print("The number is Odd.")