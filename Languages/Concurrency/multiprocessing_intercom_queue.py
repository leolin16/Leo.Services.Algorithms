# this is wrong in logic, need revising
from multiprocessing import Queue, Pool, Process
import random

def make_tuple(queue):
    num = random.randint(1, 9)
    queue.put(('Hi ', num))
    print(queue.get())

def make_string(queue):
    tup = queue.get()
    result = ''
    substr, num = tup
    for _ in range(num):
        result += substr
    queue.put(result)

if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=make_tuple, args=(queue,))
    p2 = Process(target=make_string, args=(queue,))
    p1.start()
    p2.start()