Strings can be compared via >, >=, <=, <
Each ascii code will be compared

Walrus operator assigns in an expression
In terms of order, it assigns last once the whole
expression is evaluated.



Formatting specifiers for interpolated strings

print(f"My balance is {bal:,.2f}")

[alignment][width][,][.precision][type]

# Magic numbers
amount = balance * 0.0069

What is 0.0069?
When we return to this line, we won't have a clue.
So it is good practice to comment what these strange numbers do.
Or use a named constant.

INTEREST_RATE = 0.0069
amount = balance * INTEREST_RATE


# Turtle

Outside of the IDLE program,
the turtle window will close instantly once the drawing is finished.

Add turtle.done() once the drawing is finished to keep the window open.



# Loops:
Total number of iterations in a loop =
    inner loop iterations * outer loop iterations
    
for i in range(900):
    for x in range(2):
        pass
        
900*2 = 1800

for i in range(900):
    for x in range(2):
        for z in range(9):
            pass

900*2*9 = 162000


# Else clause in a while / for loop

The else only runs if execution of the loop ended without the use of `break`.
If there is no `break` statement, the else is not a useful control flow.

# Files

file.seek(bytes_forward) -- move the cursor by the number of bytes given
file.write() -- write the whole file
rstrip() -- remove \n from line

file.read() -- read the whole file into memory
file.readline() -- read the next line (moves the cursor forward)


# File modes

+
    add a newline to each write
w
    overwrite the entire file if it exists
    write everything at once to a new file
a
    append new lines to an existing file
    create a new file to append to if one doesn't exist
    

readline() returns an empty string
when it attempts to read farther than the
maximum number of lines

Numbers must be converted to strings before
being written (this usually occurs automatically
with f string so idk about regular stuff ill have to test)

# Open multiple files at once

Heeyyyaaa

with open('file1.txt', 'r') as input_file,
     open('file1.txt', 'w') as output_file:
    # do work here
    
    
# List and Tuples

Tuples are faster for python to process, since they are immutable.

.sort() -- sort a list by ascending or descending order
.remove(value) -- remove the first occurence of value in the list (ltr)

del my_list[2] -- remove an item of a list based on its index


# String methods

Invalid splice indices do not raise an error.
This is because it rolls over/ends at the start and finish, thus there are no invalid indices.

a = 'asdjasld'
a[-12414124:89128048080:44]

# Dictionaries

Key order is unsorted. But we can use SortedDict

.clear()
    clear all dictionary key value pairs.
    
del dict[key]
    remove a key value pair
    
.get(key, default_value)
    if a value for key exists, return it.
    if not, return the default_value.
    
    doesn't raise an error if key can't be found.
    
.items()
    returns key value pairs within a tuple.
    acts like a view. this means that any update to the dictionary
    will be reflected in the .items() collection as well.
    
.keys()
    return all the dictionary keys
    [?] is it a view?
    
.values()
    return all dictionary values
    [?] is it a view?
    
.pop(key, default_value)
    delete and return the value for key.
    if key isn't found, return default_value.
    
.popitem()
    return the most recently added item as a key,value pair tuple
    returns a key,value pair as tuple.
    
# The new age Dictionary operations

merged_dict = dict1 | dict2

Dictionary Merge Operator (|)
    Combine both operands on either side of the operator into one dictionary
    
    If the same key exists in both dictionaries, only the key,value pair
    for the second operand (dict2 in the example case) will be kept.
    
Dictionary Update Operator (|=)
    