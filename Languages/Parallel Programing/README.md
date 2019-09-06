# Parallel Processing

Best suited for CPU intensive tasks like:

- String operations
- Search algorithms
- Graphics processing
- Number crunching algorithms

## Models

1. Flynn's Taxonomy

| Data Stream |    Instruction     | Streams  |
| :---------: | :----------------: | :------: |
|             |       Single       | Multiple |
|   Single    | SISD(old computer) |   MISD   |
|  Multiple   |     SIMD(GPU)      |   MIMD   |

2. Parallel Programming Model

   - Single Program, Multiple Data (SPMD)
   - Multiple Program, Multiple Data (MPMD)

## Memories

1. Shared Memory - not good at scaling, adding new processors will add load to the shared memory bus, global address space
   1. Uniform memory access (UMA) - CPUs can access memory equally fast, like SMP (Symmetric Multiprocessing System with a System Bus to access Main Memory for CPUs which have their own cache memory fast enough but needs to handle cache cohierency)
   2. Non-uniform memory access (NUMA) - connecting multiple SMP system with system bus on top of multiple SMP system that access their Main Memory seperately, some processors access quicker to some part of the memory than others
2. Distributed Memory - local address space, main memory for each CPU, connected via network for each CPU, programmer shall be responsible to define how the values should be sync throughout the system -> bad at communication, but scalable. most super comupters use some form of distributed memory or hubrid solution

## Process - instance of a program executing

A process consists of its code, data and state info
Each process has its own memory address space
Multiple processes are good for distributed system

for Java, each JVM instance is a separate, independent process with application executing in it

### Process Structure

    1. Shared code
    2. Shared data
    3. Thread 1 + Thread 2 + Thread 3

### inter process communication (IPC)

    1. Sockets and pipes
    2. Allocating special interprocess Shared Memory
    3. Remote Procedure Calls

## Threads - tiny processes

A thread is an independent path of execution
Subset of a process
Operating system schedules threads for execution
Threads are lightweight, require less overhead to create and terminate
Operating system can switch between threads faster than processes

## Concurrency - Dealing with multiple things at once (program structure) (for one core cpu, falke parallel)

Ability of a Program to be broken into parts that can run independentyly of each other

Fake Parallel: for 1 processor, concurrency means, running process/thread 1 -> running process/thread 2 -> running process/thread 1 -> running process/thread 2

True Parallel: for more than or equal to 2 processors

## Parallel - Doing multiple things at once (simultaneous execution) (not possible for one core cpu)

Good for task like UI processing
Good for computational tasks like Matrix Multiplication (huge task can be seperated into sub tasks)

## Python

Concurrent Python threads -> OK
Parallel Python threads -> NG due to GIL global interpretor lock (mechanism that limits python to only execute one thread at a time)

Interpreter compile code into intermediate Bytecode, then run with VM along with other libs

CPython uses GIL for thread-safe operation
Jython/IronPython(.net)/PyPy-STM do not have GIL

CPython thread model is good for IO-intensive tasks, but GIL will limits CPU-bound applications

Implement parallel algorithms as external library functions

To keep everything in python - use the python multiprocessing package

### Thread model

no matter how much the threads you've spinned up, max cpu occupation can only be up to 1 core due to GIL
[Multi Processing](https://docs.python.org/3/library/threading.html)

### multiproocessing

[Multi Processing](https://docs.python.org/3/library/multiprocessing.html)
`if __name__ == '__main__':` is important, because every process has its __name__ variable, and the main thread of the main process only is __main__

## Scheduling

Context Switch (register state for each process)

Algorithms
    1. first come first served
    2. shortest job next
    3. priority
    4. shortest remaining time
    5. round-robin
    6. multiple-level queues

## Thread lifecycle

New -> (Start) -> Runnable -> (waiting) -> Blocked -> (resume) -> Runnable -> (done or abnormally aborted) -> terminated

Methods:
    1. join() : wait until another thread completes its execution, own thread will enter blocked state, when resuming is continue executing
    2. set `<thread name>.daemon = True` before start() : daemon thread to be declared, will not hold the main thread if the daemon theread itself is not finished, but will abruptly exited along with the main thread

## Create Thread

1. define function and pass it to the target parameter of the constructor method of the thread
2. define a class which inherit threading.thread and override its run method (what about __init__ method?)

## Data Race

### recognition

1. schedule issue
2. happened for a simple += statement, since it requires read-modify-write process

### Mutex (mutual exclusion)

1. acquiring thread lock is an atmic action (no interference can happen)
2. Reentrant(recursive) mutex - can be locked multiple times by the same process or thread, and must be unlocked the same amount of times

### Deadlock

some thread want to lock the mutex that is already locked by itself and no other threads can unlock it, this is called a deadlock. often happend with nested function with lock/unlock logic duplicated inside or outside

another situation is that each member is waiting for another member to take action(dining philosipher)

can be prevented by :
1. reentrant mutex - a must-use method when writing recursive function
2. refactor the critical section function to be recognizable, lock/unlock can only be coded targeting these recognizable functions
3. when multiple locks are involved
   1. Lock ordering
   2. lock timeout - if acquiring all locks exceeds the limit time, then backup and free all locks taken and wait for a random amount of time and retry.
4. put critical section in try block (along with finally and exception) or "with" block to prevent from not releasing the locks due to unexpected error  

### Lock

1. Threading.Lock() can be release by a different thread
2. Threading.RLock() can only be release by the owning thread
    multiple threads acquire() and release() mutually is dangerous. can easily create problem, like release first, the python will crash when release an unlocked critical section
3. Try Lock - non-blocking version of the acquire method for mutex, \<some lock>.acquire(blocking=Flase) will immediately returns True/False
4. Read-Write Lock, good for readers > writers, shared reader + exclusive writer
    pip install readerwriterlock

### livelock

often happened during process of preventing deadlock - overly polite

solution: randomly chosen