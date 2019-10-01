# Concurrency

## Install packages

> conda install -n test-venv --file .\requirements.txt

## test run the code

> pytest

## Category

### Threading - only good for IO bound operations, due to GIL in python

1. > import threading
2. > def do_some_work(val):
3. > &nbsp;&nbsp;&nbsp;&nbsp;print("doing some work in thread")
4. > &nbsp;&nbsp;&nbsp;&nbsp;print("echo: {}".format(val))
5. > &nbsp;&nbsp;&nbsp;&nbsp;return
6. > val = "text"
7. > t = threading.Thread(target=do_some_work, args=(val,))
8. > t.start()
9. > t.join()

class threading.Thread(group=None,
                       target=None,
                       name=None,
                       args=(),
                       kwargs={},
                       daemon=None)

#### Thread lifecycle

New -> (Start) -> Runnable[Ready <-> Running] -> (waiting) -> Blocked -> (resume) -> Runnable[Ready <-> Running] -> (done or abnormally aborted) -> terminated

#### Thread Structure

1. Shared Memory, Code, OpenFiles, network sockets -> any data/memory owned by a process can be accessed by any thread within that process
2. own registers
3. own stack - local variables within a function -> thread safe

#### Scheduler - context switch

if a newly-selected thread is from a different process, a full process switch occurs,
if a newly-selected thread is from the same process, a thread switch occurs

#### Lock

to create the lock:
> lock =threading.Lock()

to acquire()/release() the lock safely
1. use try...finally
2. with lock: ...
3. non blocking lock: if some_lock.acquire(blocking=False): ... else: ... or if some_lock.locked(): ... else: ...
4. semaphore = threading.Semaphore(num_permits) -> semaphore.acquire() -> ... -> semaphore.release() : intermal counter decrements until 0 and then any acquire will become blocked until some other threads release the lock at least once to increment the internal account to be above 0, it's like a lock pool with locks permit, default permit is 1
5. semaphore = threading.BoundedSemaphore(num_permits) not permit for more release than acquire(error thrown), while standard semaphore allows unlimited release
6. threading.Event()
7. threading.Condition -> wait()/notify()/notify_all() -> good for producer-consumer pattern
```
cond = Condition()

# Consume one item
cond.acquire()
while not an_item_is_available():
    cond.wait()
get_an_available_item()
cond.release()

# Produce one item
cond.acquire()
make_an_item_available()
cond.notify()
cond.release()
```
event/condition is not intuitive

### Queue: better over condition/event

1. put() : get blocked when uppper limit has reached until some consumer get and task_done some item to make empty room for the intend-to-put item
2. get() : get blocked when no item in the queue until there's a new item
3. task_done()
4. join()
```
from threading import Thread
from queue import Queue

def producer(queue):
    for i in range(10):
        item = make_an_item_available(i)
        queue.put(item)

def consumer(queue):
    while True:
        item = queue.get()
        # do something with the item
        queue.task_done() # mark the item as done

queue = Queue()
t1 = Thread(target=producer,args=(queue,))
t2 = Thread(target=consumer, args=(queue,))
t1.start()
t2.start()
```

### Process

one GIL for every process, from python v3.8, multiple GIL for every process(one for each interpreter)

interuptable(puased) and killable(terminated) via OS APIs
an error in a process can not bring down another process - more resilient than threads
invaluable for CPU-intensive workloads

for multiprocessing, `if __name__ == '__main__':` is required, coz new process will execute both declarative code during import stage and functions during run stage, thus without __main__, section for creating new process will recursively run

class multiprocessing.Process(group=None,
                       target=None,
                       name=None,
                       args=(),
                       kwargs={},
                       daemon=None)

a daemon process is a child process that doesn't prevent its parent process from exiting, and it will live on its own lifecycle,
a daemon process is not allowed to create its own child process

#### termination

1. is_alive() -> also exists for thread
2. terminate() -> suitable for processes not using any shared resources, finally clauses and exit handlers will not be run after forcibly killed by terminate()
3. exitcode -> 0: no error, >0: error code, <0: -1 signal * error code

#### process pool

class multiprocessing.Pool([num_processes
                            [, initializer
                            [, initargs <- can be non-picklable
                            [, maxtasksperchild ]]]]) <- periodically releasing process already run a certain amount of tasks

#### pool patterns

// map for utilizing all processes
1. map(func, iterable[, chunksize])
2. map_async(func, iterable[, chunksize[, callback]]) -> AsyncResult.get([timeout])

// apply for using one process
1. apply -> on one of the worker of the process pool
2. apply_async(fimc[, args[, kwargs[, callback[, error_callback]]]])

#### communication between processes

1. Pipe - multiprocessing.Pipe
   1. duplex
2. Queue
   1. qsize() - for both threading.Queue and multiprocessing.(Joinable)Queue
   2. put() - for both threading.Queue and multiprocessing.(Joinable)Queue: Queue.put(obj, [[block[, timeout]]])
   3. get() - for both threading.Queue and multiprocessing.(Joinable)Queue: Queue.get([block[, timeout]])
   4. empty() - for both threading.Queue and multiprocessing.(Joinable)Queue
   5. full() - for both threading.Queue and multiprocessing.(Joinable)Queue
   6. task_done - for both threading.Queue and multiprocessing.JoinableQueue
   7. join() - for both threading.Queue and multiprocessing.JoinableQueue