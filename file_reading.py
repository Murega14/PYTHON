try:
    with open(input("enter name of file in folder: ")) as file:
        print(file.read())
except:
    raise FileNotFoundError("This file wasnot found")