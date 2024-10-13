"""Exercise 5 from Chapter 8 of our textbook."""

import re
    
number_codes = {
    'abc': 2,
    'def': 3,
    'ghi': 4,
    'jkl': 5,
    'mno': 6,
    'pqrs': 7,
    'tuv': 8,
    'wxyz': 9,
}

# ^\d{3}-[\dA-z]{3}-[\dA-z]{4}$

def telephone_to_numeric(phone_number: str) -> str:
    """Parse a telephone number (alphanumeric chars or numeric digits),
    and return a numeric phone number."""
    
    for digit in phone_number:
       pass
    
    
message = """
Enter a phone number in alphanumeric
or number values in the format XXX-XXXX-XXXX:
> """

user_input = input(message)

