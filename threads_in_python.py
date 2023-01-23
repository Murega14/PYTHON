#thread- slow of execution, like a separate order of instructions
# each thread  takes a turn running to achieve concurrency
#GIL(global interpreter lock) - allows only one thread to hold control of the python interpreter

#cpu bound = program/task that spends most of its internal events(cpu intensive) - use multiprocessing
#io bound - program/task that waits for external events(web threading, user input) - use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you're done eating breakfast")

def drink_coffee():
    time.sleep(4)
    print("done drinking coffee")

def study():
    time.sleep(6)
    print("done studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())