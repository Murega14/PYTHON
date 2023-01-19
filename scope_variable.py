#scope is a region that a variable is recognized

name = "Bravin" #global scope and is available everywhere
#you can have variables with the same name in both global and local


def display_name():
    name = "Ted" #local scope and only available in this function
    print(name)
display_name()
print(name)

#variables are accesed in the following order
"""Local
    Enclosed
    Global
    Built-in"""
#Ted is printed out first before Bravin