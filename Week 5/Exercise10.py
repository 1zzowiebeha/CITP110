"""Exercise #10 from Chapter 5 of our textbook."""

from typing import Any 

# Note: Re-used function from last week.
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
            
            # Return the user input converted to the desired type
            return user_input


# Type hint explanation: take a float value, and return a float.
# Type hints aren't enforced, but are helpful to readers and
# .. type checkers or static analysis tools.
def feet_to_inches(ft: float) -> float:
    return ft * 12


# Or for a super crazy type-hinted lambda function:
# from typing import Callable 
# ft_to_in: Callable[[float], float] = lambda ft: return ft * 12

prompt = "\nPlease Enter the number of ft you want to convert to inches:\n> "
user_input = prompt_user(prompt, float)

# Prompt if and until a positive number is entered.
while user_input < 0:
    print("Error: Number must be greater than 0.")
    user_input = prompt_user(prompt, float)

print(f"\n{user_input}ft is equal to {feet_to_inches(user_input):.2f} inches.")