"""Exercise 5 from Chapter 8 of our textbook."""

import string
import re

MESSAGE = """
Enter a phone number in alphanumeric
or number values in the format XXX-XXXX-XXXX:
> """

PHONE_REGEX_PATTERN = r"^\d{3}-[\dA-z]{3}-[\dA-z]{4}$"

PHONE_NUMBER_CODES = {
    'abc': 2,
    'def': 3,
    'ghi': 4,
    'jkl': 5,
    'mno': 6,
    'pqrs': 7,
    'tuv': 8,
    'wxyz': 9,
}


def telephone_to_numeric(phone_number: str) -> str:
    """Parse a telephone number (alphanumeric chars or numeric digits),
    and return a numeric phone number."""
    # Check if number is in correct format:
    if not re.match(PHONE_REGEX_PATTERN, phone_number):
          raise Exception("Error: An invalid phone number format was passed.")
    
    # Allow for string character mutation
    chars = list(phone_number)
    
    for index, char in enumerate(chars):
       char = char.lower()
       
       if char in string.ascii_lowercase:
            for letter_set in PHONE_NUMBER_CODES.keys():
                 if char in letter_set:
                      # Change alphabet character to corresponding number
                      chars[index] = str(PHONE_NUMBER_CODES[letter_set])
    
    # Concat all chars into one string
    return ''.join(chars)
            

if __name__ == "__main__":

    user_input = input(MESSAGE)
    
    print(telephone_to_numeric(user_input))