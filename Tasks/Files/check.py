#%%
# get file size in bytes
import os
os.chdir('/Users/leolin/Projects/Leo.Services.Algorithms')
currentFolder = os.getcwd()
tempFilePath = os.path.join(currentFolder, 'README.md')
print("file size: ", os.path.getsize(tempFilePath))

# get sub files/folders list within a folder
print("file list :", os.listdir(currentFolder))

# check if some path exists or not
print(os.path.exists(currentFolder))
print(os.path.exists(tempFilePath))

# check if some path is a file or not
print(os.path.isfile(tempFilePath))

# check if some path is a directory or not
print(os.path.isdir(currentFolder))
#%%
