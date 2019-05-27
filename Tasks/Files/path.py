#%%
import os
# get current directory
os.chdir('/Users/leolin/Projects/Leo.Services.Algorithms')
currentFolder = os.getcwd()
# join file path, returns \foo\fighter or foo/fighter
tempPath = os.path.join(currentFolder, 'README.md')
print(tempPath)
# split path into 2 elements tuple
print(os.path.split(tempPath))
# split path by seperator into a string list
print(tempPath.split(os.path.sep))
# change to different folder
os.chdir(os.path.join(currentFolder,'Tasks'))
currentFolder = os.getcwd()
print(currentFolder)
# get parent directory
print(os.path.dirname(currentFolder))
