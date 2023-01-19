# High order functions are functions that either:
#   1. accept a function as an argument or,
#   2. return a functions
#in python functions can also be treated as objects()

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Python Is So Cool")
    print(text)

hello(loud)
hello(quiet)
print()

#-----------------------------------------------------------------------------
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(24))