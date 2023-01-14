#*args is a parameter that packs all arguments in atuple
#useful so that a function can accept multiple arguments
#name args isnt as important as the asterist(*)

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(99, 66, 43, 25, 99))
