"""Algorithm workbench #7 from Chapter 6 in our textbookl."""

import os


def remove_user_from_file(file_name: str, user: str) -> bool:
    """Remove the passed line of text from the file.
    Returns True if successful, False if no line was found."""
    # Read and write without truncating file upon read
    with open(file_name, "r+", encoding="utf-8") as file_object:
        # Loads entire file into memory.
        # Not very efficient. See better methods here:
        # https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
        lines = file_object.readlines()
        
        if not lines:
            print('File is empty.')
            return False
        
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
            # Go back to the start of the file to write from byte 0
            # instead of at the end of the file.
            # (i'll have to read up on how this works)
            file_object.seek(0)
            # Rewrite the file without the removed line
            file_object.writelines(lines)
            return True
        else:
            return False
        
        
if __name__ == "__main__":
    # If you run a python script from the commandline,
    #   the current working directory will default to your current
    #   directory. This can result in files being written/read
    #   in the wrong folder.
    # Here, we explicitly set where exactly we want to read/write the file.
    # This is a common problem I've faced when working with files,
    #   and I usually have to re-discover the solution every time.
    # So I'll put this here and refer back when stuck :D 
    file_path = os.path.join(os.getcwd(), 'Week 6/students.txt')
    
    username = 'John Perz'
    success = remove_user_from_file(file_path, username)
    if success:
        print("Removed", username)
    else:
        print(username, "not found.")