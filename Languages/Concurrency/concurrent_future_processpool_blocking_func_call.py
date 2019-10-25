# blocking for recursive? no performance improvement on this
import concurrent.futures
import time
import asyncio

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

async def main_async(loop, executor, n):
    print('creating executor tasks in async')
    start = time.perf_counter()
    n_factorial = await loop.run_in_executor(executor, factorial, n)
    end = time.perf_counter()
    print('The factorial of {} is {}'.format(n, n_factorial))
    print("calculation takes {} seconds in async".format(end - start))

def main(n):
    print('creating executor tasks in traditional mode')
    start = time.perf_counter()
    n_factorial = factorial(n)
    end = time.perf_counter()
    print('The factorial of {} is {}'.format(n, n_factorial))
    print("calculation takes {} seconds in traditional mode".format(end - start))

if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=1)
    loop = asyncio.get_event_loop()
    n = 200
    try:
        loop.run_until_complete(main_async(loop, executor, n))
    finally:
        loop.close()
    
    main(n)