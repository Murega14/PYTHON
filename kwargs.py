#**kwargs is a parameter that packs all aguments into a dictionary

def hello(**names):
    print("Hello", end=" ")
    for key, value in names.items():
        print(value, end=" ")

hello(title = "Mr.", first="Bravin",last="Murega")