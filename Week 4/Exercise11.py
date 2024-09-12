"""Exercise #11 from our textbook."""

from typing import Any


# My type hinting skills aren't the greatest, but this is a good start
# .. for a function signature:
def prompt_user(question: str, cast_type: Any) -> Any:
    """Prompt the user for input until they enter
    a value of the desired type.
    
    This will work with str, int, float, and a class
    that takes user_input and converts it somehow.
    
    I could improve this by researching more.
    This article looks like fun:
    https://adamj.eu/tech/2021/07/06/python-type-hints-how-to-use-typing-cast/
    """
    while True:
        # I could use the walrus operator in the while loop,
        # .. but if the user inputs the string "",
        # .. this value will evaluate to False, and so the loop will end.
        # This is a better approach to validate empty input:
        user_input = input(question)
        
        # No value entered? Prompt again
        if user_input == "" or user_input.isspace():
            print(f"\nError: Please enter a numeric value.\n")
            continue

        try:
            # Similar to int(user_input) but for any
            # .. generic type
            user_input = cast_type(user_input)
        except ValueError:
            print(f"\nError: Entered invalid value. Expected a(n) {cast_type.__name__}.\n")
        else:
                
            # Validate positivity of input    
            if user_input < 0:
                print(f"\nError: Please enter a positive numeric value.\n")
                # Prompt user again
                continue
            
            # Return the user input converted to the desired type
            return user_input
        
        
DESIRABLE_DAILY_HOURS = 8

total_slept_debt: float = 0
for day in range(1, 8):
    hours_slept = prompt_user(f"Day {day}: How many hours did you sleep?: ", float)
    sleep_debt = DESIRABLE_DAILY_HOURS - hours_slept
    
    # User slept more than 8 hours. There is no debt so clamp to 0
    if sleep_debt < 0:
        sleep_debt = 0
        
    total_slept_debt += sleep_debt
    
    
if total_slept_debt == 0:
    print("\nYou slept 8 hours per day. #Super #Jealous #Sleeper")
else:
    print(
        "Total of difference between hours slept during day & 8 hours: ",
        total_slept_debt
    )