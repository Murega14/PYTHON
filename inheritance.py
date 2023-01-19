class Animal:
    alive = True

    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")

class Rabbit(Animal):
    def swim(self):
        print("The rabbit can't swim")

rabbit = Rabbit()

print(rabbit.alive)
rabbit.swim()