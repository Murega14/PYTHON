#zip(*iterable) = aggregate elements from two or more iterables(list, tuples,etc)
#creates a zip object with paired elements stored in tuples for each element

usernames = ["ted", "muregzzzz", "killua"]
passwords = ["vixenvixen", "crazyinlove", "boobsandroses"]

users = dict(zip(usernames, passwords))

for key,value in users.items():
    print(key + " : " + value)