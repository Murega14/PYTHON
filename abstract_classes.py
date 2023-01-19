#prevents a user from creating an object of that class
#also compels a user to override abstract methods in a child class

#abstract class = a class which contains one or more abstract classes
#abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("the car is moving")

class Motorcycle(Vehicle):
    def go(self):
        print("the motorcycle is moving")

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()