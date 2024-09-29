"""Exercise #6 from Chapter 6 in our textbook."""

with open('numbers.txt', 'r+') as file_object:
    # loads the whole file into memory (expensive!)
    lines = file_object.readlines()

    sum = 0
    average = 0

    for line in lines:
        try:
            line_num = int(line)
        except ValueError:
            # non-numerical value found. skip line
            continue
        else:
            sum += line_num
            
    average = sum / len(lines)
    
    # Round to two places
    print(f"{average:.2f}")