# sort() method = used with lists
#sort() function = used with iterables

students = ("ted", "john", "bravin", "jeff")
sorted_students = sorted(students, reverse=False)

for i in sorted_students:
    print(i)

#-------------------------------------------------------------------------------
stud = [("ted", "A", 88),
        ("john", "B", 60),
        ("bravin", "A", 79),
        ("jeff", "B", 69)]

grade = lambda grades:grades[1]
stud.sort(key=grade, reverse=True)

for i in stud:
    print(i)