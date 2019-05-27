#%%
import shelve
shelf = shelve.open('config')
cfg = ['option1', 'option2']
shelf['options'] = cfg
shelf.close() # store the values in the shelf and close it

shelf = shelve.open('config')
print(shelf['options'])
shelf.close()
