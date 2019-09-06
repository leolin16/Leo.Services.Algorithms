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