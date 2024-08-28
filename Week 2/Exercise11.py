"""Exercise 11 from Chapter 2 of our textbook."""


if __name__ == "__main__":
    print("Welcome to the female:male ratio calculator.\n")
    print("Note: Inputs must be integer values (ex. 0, 1, 2, 3)")
    
    try:
    males = int(input("Please enter the number of males in the class:\n> "))
    females = int(input("Please enter the number of females in the class:\n> "))
    
    total = males + females