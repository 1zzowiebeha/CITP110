"""Exercise #1 from Chapter 6 in our textbook."""

# Make sure to run this file where a numbers.txt file
#   exists.
# Todo: Look to see if numbers.txt exists before opening
#       Use absolute filepaths to avoid reliance on commandline
#       working directory location.

with open('numbers.txt', 'r+') as file_object:
    # loads the whole file into memory (expensive!)
    lines = file_object.readlines()

    for line in lines:
        # Each line has its own \n. I could strip each line,
        #   or use end='' to remove the extra \n added by print().
        print(line, end='')
        
        