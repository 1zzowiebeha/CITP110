"""Code for Exercise 16 from the textbook."""

################
# Exercise 16: #
################

try:
    year = int(input("Please enter a year:\n> "))
except ValueError:
    print("Error: The year you entered was not a number.")
else:
    # At first I combined the following two conditionals,
    # .. (year % 100 == 0 and year % 400 == 0),
    # .. but got incorrect results, so I read the directions
    # .. more and added a new conditional tree under year % 100.
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
        
    if leap_year:
        print(f"In {year}, February has 29 days.")
    else:
        print(f"In {year}, February has 28 days.")
        