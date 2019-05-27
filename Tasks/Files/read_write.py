#%%
# Types of files
# 1) plain text files
# 2) binary files
# steps:
#   1) open()
#   2) read() or write()
#   3) close()

import os
os.chdir('/Users/leolin/Projects/Leo.Services.Algorithms')
currentFolder = os.getcwd()
tempFilePath = os.path.join(currentFolder, 'test.txt')

# read files
if os.path.exists(tempFilePath):
    myfile = open(tempFilePath, 'r')
    myfile.read()
    myfile.readlines()
    myfile.close()

# write doesn't automatically write change line chars, print does
# write files in overwritting mode
myfile = open(tempFilePath, 'w')
myfile.write('some content...\n')
myfile.close()

# write files in appending mode
myfile = open(tempFilePath, 'a')
myfile.write('some other content...\n')
myfile.close()

#%%
