# Concurrency

## Install packages

> conda install -n test-venv --file .\requirements.txt

## test run the code

> pytest

## Category

### Threading

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

to acquire/release the lock safely
1. use try...finally
2. with lock: ...
3. non blocking lock: if some_lock.acquire(blocking=False): ... else: ... or if some_lock.locked(): ... else: ...
4. semaphore = threading.Semaphore(num_permits) -> semaphore.acquire() -> ... -> semaphore.release() : intermal counter decrements until 0 and then any acquire will become blocked until some other threads release the lock at least once to increment the internal account to be above 0, it's like a lock pool with locks permit, default permit is 1
5. semaphore = threading.BoundedSemaphore(num_permits) not permit for more release than acquire(error thrown), while standard semaphore allows unlimited release
6. threading.Event()
7. threading.Condition -> wait()/notify()/notify_all() -> good for producer-consumer pattern

### Queue: better over condition/event

1. put()
2. get()
3. task_done()
4. join()
