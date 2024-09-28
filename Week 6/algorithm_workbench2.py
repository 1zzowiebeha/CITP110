"""Algorithm workbench #2 from Chapter 6 in our textbook."""

# Note: your terminal working directory will
#   .. determine where the output file is created!
with open('number_lists.txt', 'w') as file_object:
    # list comprehension:
    numbers = [i for i in range(1,101)]
    file_object.writelines(numbers)