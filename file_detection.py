import os

path = "/home/nyaweed/classes and objects"

if os.path.exists(path):
    print("The location exists")
    if os.path.isfile(path):
        print("This is a file")
else:
    print("This location doesn't exist")

#to check for a directory use os.path.isdir(path)