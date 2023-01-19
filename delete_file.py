import os

path = "text2.txt"
try:
    os.remove(path)
    print("File was deleted")

except FileNotFoundError:
    print("That file was not found")

#os.rmdir(path) deletes directories and folders that are empty
#to remove a directory that isnt empty
#import shutil
#shutil.rmtree(path)  """this deletes EVERYTHING"""