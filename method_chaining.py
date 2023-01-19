#methdd chaining is used to call multiple methods sequentially

class Car:
    def turn_on(self):
        print("start the engine")
        return self
    def drive(self):
        print("drive the car")
        return self
    def brake(self):
        print("brake the car")
        return self
    def turn_off(self):
        print("turn off the engine")
        return self

car = Car()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()