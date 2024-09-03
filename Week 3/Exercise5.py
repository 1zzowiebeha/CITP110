"""Code for Exercise 5 from the textbook."""

###############
# Exercise 5: #
###############

# Lambda expression, a function
# .. with smaller syntax
weight = lambda mass: mass * 9.8

try:
    input_mass = float(input("Please enter the mass:\n> "))
except ValueError:
    print("Error: The value you entered was not a number.")
else:
    calculated_weight = weight(input_mass)
    
    if calculated_weight > 500:
        print(f"Weight: {calculated_weight:.2f} newtons. The weight is too heavy.")
    elif calculated_weight < 100:
        print(f"Weight: {calculated_weight:.2f} newtons. The weight is too light.")
    else:
        print(f"Weight: {calculated_weight:.2f} newtons. The weight is just right.")