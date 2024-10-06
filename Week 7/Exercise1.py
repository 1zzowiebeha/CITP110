"""Exercise 1 from Chapter 7 of our textbook."""

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

# valid_numbers = [x for x in numbers if 100 < x and x > 0]
valid_numbers = []

for x in numbers:
    if 100 < x and x > 0:
        valid_numbers.append(x)

average = sum(valid_numbers) / len(valid_numbers)
print("\nAverage of valid numbers:", average)