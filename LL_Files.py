# Linkedin Learning Files Challenge
# Calculate and return the total number of bytes of the text file sizes within the current working directory.
# Only include text files that end with ".txt" in your calculation. Other files should be ignored

import os

def file_info():
    totalbytes = 0
    cwd = os.getcwd()
    dirlist = os.listdir(cwd)
    # Loop through all files within the current working directory checking the type.
    for entry in dirlist:
        # If the item is a File, and has a .txt extension, then pull the file size and add it to the totalbytes variable.
        if os.path.isfile(entry) and entry.endswith(".txt"):
            file_size = os.path.getsize(entry)
            totalbytes += file_size
    print(totalbytes)
    return(totalbytes)

if __name__ == "__main__":
    file_info()
