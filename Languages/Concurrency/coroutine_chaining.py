import asyncio

async def perform_task():
    print('performing task')
    print('waiting for result1')
    result1 = await subtask1()
    print('waiting for result2')
    result2 = await subtask2(result1)
    return (result2, result2)

async def subtask1():
    print('perform subtask 1')
    return 'result1'

async def subtask2(arg):
    print('perform subtask 2')
    return 'result2 relies on {}'.format(arg)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(perform_task())
loop.close()