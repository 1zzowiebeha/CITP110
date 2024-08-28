"""Exercise 11 from Chapter 2 of our textbook.
For fellow students: If all of this looks scary and crazy,
don't worry. I have programmed in python for many years so I am
using advanced techniques like type hinting, regex examples, etc."""


# This function uses type hints, specifically union types.
def strip_unwanted_zeros(numeric: float | int) -> float | int:
    r"""Remove trailing 0s from a float to turn it into an int representation.
    Removes all captured characters in ^(?:\d+)(\.0+)$ regex.
    
    We convert to a string to perform the character manipulations.
    Then we return the correct numeric type back to the user.
    
    Ex. if we receive 45.00, we would like just 45.
        .. But if we receive 45.65, we want 45.65.
        .. If we receive an int like 32, we want 32."""
    if isinstance(numeric, float):
        stripped = str(numeric).rstrip("0").rstrip(".")
        
        # Only integer digits were found
        if stripped.isdigit():
            return int(stripped)
        # A . character was detected, thus there are decimal digits
        else:
            return float(stripped)
    # Do nothing for ints
    elif isinstance(numeric, int):
        return str(numeric)


if __name__ == "__main__":
    print("\nWelcome to the female:male ratio calculator.\n")
    print("Note: values must be integer values (ex. 0, 1, 2, 3)")
    
    try:
        males = int(input("Please enter the number of males in the class:\n> "))
        females = int(input("Please enter the number of females in the class:\n> "))
    except ValueError:
        print("\nError: A value you entered was not a number.")
    else:
        if males < 0 or females < 0:
            print("\nError: A value you entered was less than 0.")
        else: 
            total = males + females
            
            males_percentage = (males / total) * 100
            females_percentage = (females / total) * 100
            
            formatted_male_percent = strip_unwanted_zeros(males_percentage)
            formatted_female_percent = strip_unwanted_zeros(females_percentage)
            
            print(f"\nTotal: {total}")
            print(f"Males: {males}, {formatted_male_percent:.2f}%")
            print(f"Females: {females}, {formatted_female_percent:.2f}%")