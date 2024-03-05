# File Converter with Python
# This code allows you to convert file content using Python. (csv, svg, txt, log etc.)
# Run the project:
#     python convertfiles.py (for Windows)
#     python3 convertfiles.py (for Linux)

import os

def convert_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".svg"):
            input_file = os.path.join(directory, filename)
            output_file = os.path.join(directory, filename + ".csv")
            # File Convert
            with open(input_file, 'r') as f:
                content = f.read()
            with open(output_file, 'w') as f:
                f.write(content)
            print(f"{input_file} converted and as a {output_file} saved.")

if __name__ == "__main__":
    directory = "."  # Sets the directory in which it is executed for processing.
    convert_files_in_directory(directory)
