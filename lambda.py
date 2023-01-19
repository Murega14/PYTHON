#lambda function - function written in 1 line using lambda keyword
#it accepts any no. of arguments, but has only one expresion
# syntax is (lamda parameters:expression)

double = lambda x:x * 2
print(double(5))
add = lambda x, y, z: x + y + z
print(add(5, 6, 7))
full_name = lambda first_name, last_name: first_name + last_name
print(full_name("Bravin", "Murega"))