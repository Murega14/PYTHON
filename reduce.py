#reduce() = apply a function to an iterable and reduce it to a single cumulative value
#performs function on first two elements and repeats the process until 1 value remains
#reduce(function, iterable)

import functools

letters = ["h", "e", "l", "l", "o"]
word = functools.reduce(lambda x, y:x + y, letters)
print(word)