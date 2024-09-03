"""Code for Exercise 1 from the textbook."""

###############
# Exercise 1: #
###############


try:
    number = int(input("Please enter a number:\n> "))
except ValueError:
    print("Error: The value you entered was not a number.")