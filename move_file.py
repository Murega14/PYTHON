import os

source = "text.txt"
destination = "text2.txt"

try:
    if os.path.exists(destination):
        print("there is a file there already")
    else:
        os.replace(source,destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source+" was not found")