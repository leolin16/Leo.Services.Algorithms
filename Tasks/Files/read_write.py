#%%
# Types of files
# 1) plain text files
# 2) binary files
# steps:
#   1) open()
#   2) read() or write()
#   3) close()

import os
import asyncio
import aiofiles

async def open_file_async(filePath):
    # read files in async
    if os.path.exists(filePath):
        async with aiofiles.open(filePath, mode='r') as myfile_async:
            contents_async = await myfile_async.read()
            print("async file :", contents_async)
            await myfile_async.readlines()

async def write_file_async(filePath):
    async with aiofiles.open(filePath, 'w') as myfile_async:
        await myfile_async.write('some async content...\n')

os.chdir('/Users/leolin/Projects/Leo.Services.Algorithms')
currentFolder = os.getcwd()
tempFilePath_traditional = os.path.join(currentFolder, 'test_old.txt')
tempFilePath_async = os.path.join(currentFolder, 'test_async.txt')

# read files
if os.path.exists(tempFilePath_traditional):
    myfile = open(tempFilePath_traditional, 'r')
    contents_trad = myfile.read()
    print("traditional file :", contents_trad)
    myfile.readlines()
    myfile.close()

# write doesn't automatically write change line chars, print does
# write files in overwritting mode
myfile = open(tempFilePath_traditional, 'w')
myfile.write('some traditional content...\n')
myfile.close()

# write files in appending mode
myfile = open(tempFilePath_traditional, 'a')
myfile.write('some other content...\n')
myfile.close()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(write_file_async(tempFilePath_async))
    loop.run_until_complete(open_file_async(tempFilePath_async))
finally:
    loop.close()
#%%
