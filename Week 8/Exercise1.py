"""Exercise 1 from Chapter 8 of our textbook."""

if __name__ == "__main__":
    # Separate previous terminal commands from output
    print()

    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")

    print("\nHere are your initials, your address name, and your username:")

    print(fname[0].upper() + '.' + lname[0].upper())
    print(fname.title() + ' ' + lname.upper())
    print(fname[0].lower() + lname.lower())