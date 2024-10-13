"""Exercise 4 from Chapter 8 of our textbook."""

# ChatGPT helped to generate this.
# It's nice for mock data, but it makes mistakes.
# Still faster than writing it all by hand though.
MORSE_CODES = {
    ' ': ' ',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.-',
    'Z': '--..',
}


def string_to_morse_code(message: str) -> str:
    """Parse a string (alphanumeric chars or numeric digits),
    and return a string of morse code."""
    # Allow for string character mutation
    chars = list(message)
    
    for index, char in enumerate(chars):
        char = char.upper()
       
        for key in MORSE_CODES.keys():
                if char == key:
                    # Change alphabet character to corresponding morse code value
                    chars[index] = MORSE_CODES[key]
    
    # Concat all chars into one string
    return ''.join(chars)
            

if __name__ == "__main__":
    user_input = input("Please enter a string to convert into morse code: ")
    
    print(string_to_morse_code(user_input))