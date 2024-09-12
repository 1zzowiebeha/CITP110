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
        
        
speed = prompt_user("What is the speed of the vehicle in mph?: ", float)
time = prompt_user("How many hours has it traveled?: ", int)

print("Hour      Distance Travelled")
print("----------------------------")
# Upper boundary is exclusive, while lower boundary is inclusive.
for hour in range(1, time + 1):
    # I could use some interpolated string
    # .. stuff (similar to {value:.2f}) to
    # .. result in responsive output and spacing,
    # .. but this works for now.
    
    # No zero stripper for this, since my aim is to
    # .. write code that is both semi-professional and
    # .. understandable to all levels of experience
    print(f"{hour}         {hour * speed}")