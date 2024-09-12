"""Exercise #11 from our textbook."""

"""Exercise #4 from our textbook."""
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
    while user_input := input(question):
        try:
            # Similar to int(user_input) but for any
            # .. generic type
            user_input = cast_type(user_input)
        except ValueError:
            print(f"\nError: Entered value expected a {cast_type.__name__}.")
        else:
            # Return the user input converted to the desired type
            return user_input