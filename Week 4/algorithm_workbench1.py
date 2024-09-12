"""Algorithm workbench assignment #1 from our textbook."""

# type hint syntax
product: float = 0

while product < 100:
    try:
        numeric_input = float(input("Enter a number: "))
    except ValueError:
        print("Error: Entered value was not a number.")
        # begin a new iteration
        continue
    
    product += (numeric_input * 10)
    
print("Final product:", product)