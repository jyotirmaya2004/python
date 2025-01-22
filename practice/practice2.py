import os

# Specify the directory (use '.' for the current directory)
directory = '/c programming/Assignment/Assignment 9'

# List the contents of the directory
contents = os.listdir(directory)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
