# walrus operator :=
# assigns values to variables as part of a larger expression

#now the following code(commented)
# foods = list()
# while True:
#       food = input("what food do you like?: ")
#       if food == "quit":
#           break
#       foods.append(food)

# now using a walrus operator
foods = list()
while proceed := input("will you have more?") != "quit":
        food = input("enter your favorite food: ")
        foods.append(food)
        
        
print(foods)
