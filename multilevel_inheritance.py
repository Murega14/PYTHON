#multi level inheritance is when a child class inherits from another child class

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("the animal is eating")

class Dog(Animal):
    def bark(self):
        print("the dog is barking")

dog = Dog()
print(dog.alive)     #inherited from the parent class Organism
dog.eat()           #inherited from the child class Animal
dog.bark()
