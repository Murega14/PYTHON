#*args is a parameter that packs all arguments in atuple
#useful so that a function can accept multiple arguments
#name args isnt as important as the asterist(*)

x = int(str(input("enter a number ")))
y = int(str(input("enter a number ")))
z = int(str(input("enter a number ")))
   
def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(0,x,y,z))
