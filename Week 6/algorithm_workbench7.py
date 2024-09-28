"""Algorithm workbench #7 from Chapter 6 in our textbookl."""

def remove_user_from_file(file_name: str, user: str) -> bool:
    """Remove the passed line of text from the file.
    Returns True if successful, False if no line was found."""
    with open(file_name, "w+") as file_object:
        # Loads entire file into memory.
        # Not very efficient. See better methods here:
        # https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
        lines = file_object.readlines()
        
        line_to_remove = 0
        
        for line in lines:
            words = line.split(' ')
            # The last part of the line will be the score.
            # All other parts of the line will be the name.
            # Join these pieces with a space.
            name = ' '.join(words[:-1])
            
            if name == user:
                # Break out of the loop
                break
                
            line_to_remove += 1
        
        # A match was found in the file
        if len(lines) != line_to_remove:
            del lines[line_to_remove]
            # Rewrite the file without the removed line
            file_object.writelines(lines)
            return True
        else:
            return False
        
        
if __name__ == "__main__":
    username = 'John Perz'
    success = remove_user_from_file('students.txt', username)
    if success:
        print("Removed", username)
    else:
        print(username, "not found.")