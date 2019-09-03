#%% basic
def SqureIt(x):
    return x * x
print(SqureIt(2))

#%% pass functions around as parameters
def DoSomething(f, x):
    return f(x)

print(DoSomething(SqureIt, 3))

#%% lambda functions can also be passed as parameters
print(DoSomething(lambda x: x * x * x, 3))

#%%
