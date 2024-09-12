"""Algorithm workbench assignment #5 from our textbook."""

total: float = 0
numerator: float = 0

for denominator in range(30, 0, -1):
    numerator += 1
    
    product = numerator / denominator
    total += product
    
    print(f"{numerator}/{denominator} = {product}")
    
print("\nThe total is:", total)