#%%
# %config ZMQInteractiveShell.ast_node_interactivity='all'
import urllib3
import urllib3.request

print(type(urllib3))
print(type(urllib3.request))

print(urllib3.__path__)
try:
    urllib3.request.__path__ # path to show where to search for included modules
except Exception as e:
    print(e)
finally:
    print('\nthis is an example to show difference between package and module in python')

#%%
# sys.path is a list of directories python searches for modules