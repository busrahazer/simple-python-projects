file_name = "file_name"

try:
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"{file_name} don't find.")
except IOError:
    print(f"{file_name} error when read file.")
