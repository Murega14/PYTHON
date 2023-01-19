class Car():
    
    wheels = 4 #class variable

    def __init__(self, model, make, year, color):
        self.model = model   #this is an instance variable
        self.make = make
        self.year = year
        self.color = color