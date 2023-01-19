#list comprehension = a way to create a new list with less syntax
#it can mimic certain lambda functions and its easy to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if condition]
# list = [expression if/else for item item in iterable]

squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1,11)]
print(squares)

students = [100,90,60,70,60,50,40,30,0]

passed_students = [i for i in students if i >= 60]
passed_students1 = [i if i >= 60 else "FAILED" for i in students]
print(passed_students1)