"""Exercise 4 from Chapter 9 of our textbook."""

import os


# UNIQUE storage (only one occurence can exist in storage)
# UNIQUE retrieval (only one occurence is found)
#       For this case, I would use regex (.* )|( .*)
#       Unique matches will be stored.
def display_unique_words():
    """Store each word in the data within a set."""
    file_path = os.path.join(os.getcwd(), 'Week 9/data.txt')
    
    unique_words = set()
    with open(file_path, 'r', encoding="utf8") as file_object:
        lines = file_object.readlines()
        
        # Store unique words
        for line in lines:
            words = line.split(' ')
            for word in words:
                unique_words.add(word)
    
        # Store word frequency count
        # word_frequencies = {}
        # for line in lines:
        #     for word in unique_words:
        #         if word in line:
        #             if word in word_frequencies:
        #                 word_frequencies[word] = word_frequencies[word] + 1
        #             else:
        #                 word_frequencies[word] = 1
    
    print('All words within the data:')
    for word in unique_words:
        print(f'\t{word.strip()}')


if __name__ == "__main__":
    display_unique_words()