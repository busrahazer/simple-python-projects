# File Reader with Python
# This code allows you to read file content using Python.
# Run the project:
#     python readfile.py (for Windows)
#     python3 readfile.py (for Linux)

file_name = "file_name"  # Type your file name here

try:
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"{file_name} don't find.")
except IOError:
    print(f"{file_name} error when read file.")
