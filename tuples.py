#a tuple is a collection which is ordered and unchangeable
# they are used to group together related data

student = ("Bravin", 20, "male")

#methods available in tuples are
print(student.count("male"))
print(student.index("Bravin"))
#

for x in student:
    print(x)
if 20 in student:
    print("they are not minors")