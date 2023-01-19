#map() applies a function to each item in an iterable(list, tuple etc)
#map(function, iterable)

store = [("shirt", 20.00),
        ("pants", 25.00),
        ("jacket", 50.00),
        ("socks", 5.00)]

to_ksh = lambda data: (data[0],data[1]*124.10)
store_ksh = list(map(to_ksh, store))

for i in store_ksh:
    print(i)