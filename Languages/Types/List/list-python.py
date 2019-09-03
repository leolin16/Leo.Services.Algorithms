#%% get length of a list/tuple
x = [1,2,3,4,5,6]
a = (1,2,3,4,5,6)
print(len(x))
print(len(a))

#%% left slice
x[:3]

#%% right slice
x[3:]

#%% right slice
x[-2:]

#%% extend
x.extend([7,8])
x
#%% append
x.append(9)
x
#%% list of lists
y = [10,11,12]
b = (10,11,12)
listOfLists = [x,y]
listOfTuples = [a,b]
print(listOfLists)
print(listOfTuples)

#%% list element location
print(y[1])
print(b[2])
#%% sort
z = [3,2,1]
z.sort()
print(z)
z.sort(reverse=True)
print(z)

#%% split
(age, income) = "32,120000".split(',')
print(age)
print(income)

#%%
