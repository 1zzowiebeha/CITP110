"""Exercise 7 from Chapter 2 of the book."""


def miles_per_gallon(miles_driven: float,
                     gallons_used: float) -> float:
    """Calculate the number of miles one gallon of gas provides."""
    return miles_driven / gallons_used


if __name__ == "__main__":
    print("Welcome to the Miles per Gallon calculator.")
    print("This program will calculate how many miles to the gallon you get\n \
          by dividing miles driven by gallons of gas used.")
    
    try:
        miles_driven = float(input("Please enter the miles you drove:\n> "))
        gallons_used = float(input("Please enter the gallons of gas your car used:\n> "))
    except ValueError:
        print(f"\nThe value you entered was not a number. Shutting down...")
    else:
        if miles_driven < 0 or gallons_used < 0:
            print("\nA value you entered was a negative number. Shutting down...")
        else:
            mpg = miles_per_gallon(miles_driven, gallons_used)
            print(f"\nMiles per Gallon: {str(mpg)}")