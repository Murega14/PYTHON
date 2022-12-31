#if statement is a block of code that executes if it's condition is true
age = int(input("How old are you?: "))

if age >= 18:
    print("You can drink alcohol")
elif age < 0:
    print("ERROR")
else:
    print("Go back home!")

if age >= 85:
    print("Please consider going home")