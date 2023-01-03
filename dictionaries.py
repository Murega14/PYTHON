#a dictionary is a changeable, unordered collection of unique key:value pairs
# they are fast because they use hashing, allowing us to access a value quickly

capitals = {'Kenya':'Nairobi',
            'Rwanda':'Kigali',
            'Uganda':'Kampala',
            'Tanzania':'Dodoma'
            }

print(capitals.get('Kenya'))
#to print keys only
print(capitals.keys())
#to print values only
print(capitals.values())
#to add another key and value
capitals.update({'DRC':'Kinshasa'})
#to remove a key and value
capitals.pop('Tanzania')
#to print both keys and values
print(capitals.items())

#displaying everything in the dictionary using for loop
for key, value in capitals.items():
    print(key,value)