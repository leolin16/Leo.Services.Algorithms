# Concurrency

## Install packages

> conda install -n test-venv --file .\requirements.txt

## test run the code

> cd Languages\Concurrency\
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

#### process sharing state

1. Shared Memory
   1. multiprocessing.Value(typecode_or_type, *args[, lock]) # lock argument is keyword only argument

    ```python
    counter = Value('i') # shared object of type int, defaults to 0
    is_running = Value(ctypes.c_bool, False, lock=False) # shared object of type boolean, defaulting to False, unsynchronized

    my_lock = multiprocessing.Lock()
    size_counter = Value('l', 0, lock=my_lock) # shared object of type long, with a lock specified
    ```

   2. multiprocessing.Array
1. Manager Process(via proxy, can be over network, remote call) - can share more complex types but cost more time
   1. Value - Lock
   2. Array - RLock
   3. Dictionary - Event
   4. List - BoundedSemaphore
   5. Namespace - Condition
   6. Queue - Barrier

```python
multiprocessing.Manager() # spins up a new process
```

### Executor API

#### Traditional

1. Define Task - function def
2. Pass to Executor - threading.Thread/multiprocessing.Process(target=?) -> ?.start()
3. Get Result - ?.join

#### new executor api
1. submit(fn, *args, **kwargs) # schedules a function to run, non-blocking, -> result()
2. map(func, \ # uses executor worker pool to apply the passed in function to every member of the iterable or iterables concurrently
    *iterables, \
    timeout=None, # how long to wait for a task to complete\
    chunksize=1 \ # how chop up the iterable per worker
    ) -> result()
3. shutdown(wait=True) # stop accepting tasks and shutdown
   no need to call shutdown if:

   ```python
    with executor:
        ...use executor...
    ```
4. ThreadPoolExecutor(max_workers=None, thread_name_prefix='') # max_workers defaults to CPU_cores*5
5. ProcessPoolExecutor(max_workers=None) # max_workers defaults to CPU_cores

old:

```python
def sayhello(name):
    print("hello from {}".format(name))
    return
names = ["Tim", "Sarah", "Robert"]
threads = []
for name in range(names):
    t = threading.Thread(target=sayhello, args=(name, ))
    t.start()
    threads.append(t)
[t.join() for t in threads]
```

new: great for thread/process switch operations like tasks mixed with IO and CPU, or changed platforms

```python
def sayhello(name):
    print("hello from {}".format(name))
    return
names = ["Tim", "Sarah", "Robert"]
# new threadpool or processpool instance
executor.map(sayhello, names)
```

### future objects

enabling asynchronous programming

```python
future = executor.submit(func, args*) # executor acts as an actor
... do other things ...
result = future.result() # can throw exception
```

1. cancel() # attempt to cancel execution, Return True if successful
2. done() # returns True if completed or canceled successfully
3. exception(timeout=None) # returns the exception raised, if any, timeout exceeds -> raising timeout err; no exception raised -> returns None
4. add_done_callback(fn) # attached function to be called on completion or cancellation
5. module functions
   1. concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED) # fs is iterables of futurn objects
   2. concurrent.futures.as_completed(fs, timeout=None) # yield a completed future object in turn
6. result()

#### difference between asyncio.Future and concurrent.future.Future

asyncio.Future is non-blocking:

   1. > .result()
   2. > .exception()

concurrent.future.Future is blocking:

   1. > .result(timeout)
   2. > .exception(timeout)

reason is that concurrency model has blocking style is because multi-threading processing, while asyncio is almost within one single thread, thus blocking is undesirable

Inside a coroutine, if there's a future, await it.

Outside a coroutine, pass the future to the event loop via run_until_complete, the event loop will stop when the future is done

### single threaded asynchony

good for IO-bound tasks
good for event-driven arch

when using multiple threads to handle IO-bound tasks, memory overhead and context switching cost are high

dealing IO-bound tasks within one single thread is more appropriate when facing thousands of IO-bound tasks

#### event loop

is responsible for getting items from an event queue and handling it

events like Change of file state/Timeout occurring/New data at network socket

1. asyncio.get_event_loop()
2. AbstractEventLoop.run_forever()
3. AbstractEventLoop.run_until_complete(future)
4. AbstractEventLoop.stop()
5. AbstractEventLoop.close()

#### Coroutine

1. Coroutine Function

    ```python
    import asyncio
    async def delayed_hello(): # turns the function into an coroutine
        print("Hello")
        await asyncio.sleep(1) # tells the eventloop to suspend this and go to other available tasks.
        print("World!")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(delayed_hello()) # run_until_complete takes in a coroutine object and wrap it into future object in order to process it
    loop.close()
    ```

    Event Loop -> Future pending -> Coroutine starts -> Coroutine suspended when meeting await ... -> returns to future then to event loop -> await time later: event loop to future to Coroutine resumes -> Coroutine ends -> Future done -> return to event loop

2. Coroutine Object

    ```python
    CoroutineObject = CoroutineFunction()
    Future(CoroutineObject)
    # pass to event loop
    ```

3. Coroutine Chaining

a coroutine awaiting another coroutine

4. wait for multiple coroutines to be completed

```python
coroutine asyncio.wait(futures, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
# returns (DONE_FUTURES, PENDING_FUTURES)
```

5. wait for one task (automatic canceling)

```python
try:
    result = await asyncio.wait_for(task, 30.0)
except asyncio.TimeoutError:
    print('task did not complete in 30 seconds so it was canceled')
```

6. wait for iterable tasks

asyncio.as_completed(fs, *, loop=None, timeout=None)

```python
for task in asyncio.ascompleted(tasks):
    result = await task
# returns futures
```

7. returns a future that aggregates results from pasttime futures in original sequence rather than time of arrivals. can not cancel future individually, no timeout argument

```python
asyncio.gather(*coroutines_or_futures, loop=None, return_exceptions=False)
```

8. async libs: [async libs](https://github/python/asyncio/wiki/ThirdParty)
   1. > pip install aiohttp
   2. > pip install aiofiles
   3. > pip install aiomysql
   4. > pip install pg
   5. > pip install aiocouchdb
   6. > pip install aiocassandra

9. blocking in corouting
    need to delecate the callings to blocking functions in delegator
    ```python
    coroutine AbstractEventLoop.run_in_executor(executor, func, *args)
    ```
    

#### Task

a subclass of Future that is used to wrap and manage the execution of a coroutine in an even loop

a coroutine must be wrapped as a task before it can be run within the event loop

creating a task:

```python
asyncio.ensure_future(coroutine_or_future, *, loop=None)
```

or

```python
AbstractEventLoop.create_task(coroutine)
```