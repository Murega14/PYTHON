#dictionary comprehension = create dictionaries using an expression
#can replace for loops and certain lambda functions
# dictionary = {key :expression for (key,value) in iterable}
# dictionary = {key :expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}

cities_in_f = {'New York':32, 'Boston':75, 'Nairobi':69, 'Kigali':50}

cities_in_c = {key: round((value - 32)*(5/9)) for (key, value) in cities_in_f.items()}
print(cities_in_c)

weather = {'New York':"snowing", 'Boston':"sunny", 'Nairobi':"sunny", 'Kigali':"cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

desc_cities = {key: check_temp(value) for (key, value) in cities_in_f.items()}
print(desc_cities)

