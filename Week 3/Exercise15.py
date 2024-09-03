"""Code for Exercise 15 from the textbook."""

# This function uses type hints, specifically union types.
def strip_unwanted_zeros(numeric: float | int) -> str:
    r"""Remove trailing 0s from a float to turn it into an int representation.
    Removes all captured characters in ^(?:\d+)(\.0+)$ regex.
    
    We convert to a string to perform the character manipulations.
    Then we return a string to use as our percentage output.
    
    Ex. if we receive 45.00, we would like just 45.
        .. But if we receive 45.65, we want 45.65.
        .. If we receive an int like 32, we want 32."""
    if isinstance(numeric, float):
        stripped = str(numeric).rstrip("0").rstrip(".")
        
        # Only integer digits were found
        if stripped.isdigit():
            return stripped # return string
        # A . character was detected, thus there are decimal digits
        else:
            # Limit output to 2 decimal places
            return f"{float(stripped):.2f}"
    # Do nothing for ints
    elif isinstance(numeric, int):
        return str(numeric)
    
################
# Exercise 15: #
################
print("Welcome. Welcome to the super second calculator.\n")

try:
    seconds = int(input("Please enter the number of seconds to calculate:\n> "))
except ValueError:
    print("Error: The input value must be a numeric.")
else:
    if seconds >= 60:
        minutes = seconds/60
        print(f"\nMinutes: {strip_unwanted_zeros(minutes)}")
    if seconds >= 3600:
        hours = seconds/3600
        print(f"Hours: {strip_unwanted_zeros(hours)}")
    if seconds >= 86400:
        days = seconds/86400
        print(f"Days: {strip_unwanted_zeros(days)}")
        