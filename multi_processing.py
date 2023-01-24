# multiprocessing - running tasks in parallel on different cpu cores
# its better for cpu bound tasks
# multithreading is better for io bound tasks

from multiprocessing import Process, cpu_count
import time



def counter(num):
    count = 0
    while count < num :
        count += 1

def main():

    print(cpu_count())

    a = Process(target=counter, args=(125,))
    b = Process(target=counter, args=(125,))
    c = Process(target=counter, args=(125,))
    d = Process(target=counter, args=(125,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("finished in: ", abs(time.perf_counter()), "seconds")

if __name__ == '__main__':
    main()
  
