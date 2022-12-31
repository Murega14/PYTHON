#for loop is a statement that executes its block
#  of code a limited amount of times
import time

#creating a countdown timer hooray

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new Year ")