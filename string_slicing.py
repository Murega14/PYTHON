#slicing is creating a substring by extracting elements from another string
#you can use indexing[] or slice()
#[starting_point:end_point]

name = "bravin murega"
#creating a substring

first_name = name[:6]
print(first_name)
last_name = name[7:13]
print(last_name)
#in indexing the original syntax is [start:stop:step]
#if i wanted to print every 3 character in my name variable then:
funky_name = name[::3]
print(funky_name) #the first character will be printed too

#reversing the string
reversed_name = name[::-1]
print(reversed_name)

#thats all about indexing[]
#now over to slice()
website = "http://github.com"
slice = slice(7,-4) #used negative 4 so as to start counting from backwards
print(website[slice])