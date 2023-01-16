class Car:

    color = None

def change_color(vehicle, color):
    vehicle.color = color

car_1 = Car()
change_color(car_1, "red")
print(car_1.color)