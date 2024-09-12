"""Exercise #1 from our textbook."""

# results in line 4 being smaller:
prompt = "Day {0} - How many bugs did you collect?: "
total_bugs_caught: int = 0

for day in range(1,6):
    # Augmented assignment (walrus operator)
    # .. allows us to assign a variable within an expression.
    while day_catch := input(prompt.format(day)):
        # Test if the value is an int
        try:
            day_catch = int(day_catch)
        except ValueError:
            print("\nError: Entered value must be a number.\n")
            # Continue another iteration of the while loop
            # .. (prompt the user again via augmented assignment)
            continue
        # No errors? Add to the total and break out of the while loop
        else:
            # I could add another while block to test for negative values,
            # .. but maybe some bugs escaped in which negative values
            # .. make perfect sense to allow.
            total_bugs_caught += day_catch
            break

# A bug count less than zero doesn't make sense.
# .. Let's assume the user made an error
# .. and clamp it to zero.
if total_bugs_caught < 0:
    total_bugs_caught = 0
    
print("\nTotal bugs collected:", total_bugs_caught)