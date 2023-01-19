#multiple inheritance - when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("this animal flees")

class Predator:
    def hunt(self):
        print("this animal hunts")

class Fish(Predator, Prey):
    pass
fish = Fish()
fish.flee()
fish.hunt()