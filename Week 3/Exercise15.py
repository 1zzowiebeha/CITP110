"""Code for Exercise 15 from the textbook."""


################
# Exercise 15: #
################
print("Welcome. Welcome to the super second calculator.\n")

try:
    seconds = int(input("Please enter the number of seconds to calculate:\n> "))
except ValueError:
    print("Error: The input value must be a numeric.")
else:
    if seconds >= 60:
        minutes = seconds/60
        print(f"\nMinutes: {minutes:.2f}")
    if seconds >= 3600:
        hours = seconds/3600
        print(f"Hours: {hours:.2f}")
    if seconds >= 86400:
        days = seconds/86400
        print(f"Days: {days.2f}")
        