"""Exercise #17 from our textbook."""

from typing import Any


# Note: Re-used function from last week
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
        
        
def is_prime(input_num: int) -> bool:
    """Test if the input number is prime.
    
    Rules to test if a number is prime:
        1. Number must be divisible by itself.
        2. Number must be divisible by one.
        3. Number must return a remainder when divided by
            another number.
        4. Number must be positive.
    """
    
    # Check this here so that
    # .. we don't perform (-1 % 2 == 0)
    # .. and proceed as though 0 is prime
    if input_num == 0:
        return False
    
    # Must be positive.
    # If we wanted to include negative numbers as prime candidates,
    # .. we could check for positivity and use a reversed range function
    # .. to count up to 2 from the negative number.
    if input_num < 0:
        return False
    
    is_divisible_by_another = False
    
    # This test is purely to check divisibility by numbers
    # .. between 2 and (input_num - 1). (second range arg is exclusive)
    # If we include input_num, (input_num % num == 0) will always be True and
    # .. so False will return.
    # If we include 1, (input_num % 1 == 0) will always be True and
    # .. so False will return.
    for num in range(input_num - 1, 1, -1):
        if input_num % num == 0:
            return False
    
    return True


print("* Prime Number Checker *")

# Prompt the user forever
# .. (or until they press CTRL+C for a KeyboardInterrupt)
while True:
    user_input = prompt_user("\nPlease enter a number:\n> ", int)
    is_user_input_prime = is_prime(user_input)

    if is_user_input_prime:
        print(f"{user_input} is prime.")
    else:
        print(f"{user_input} is not prime.")