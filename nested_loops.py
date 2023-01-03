#nested loops is where the inner loop finishes all of its iterations first before finishing the outer loop iterations
#can be a for or while loop

rows = int(input("How many rows?: "))
column = int(input("How many columns?: "))
symbol = input("What symbol do you want to use?: ")

for i in range(rows):
    for j in range(column):
        print(symbol, end="")
    print()