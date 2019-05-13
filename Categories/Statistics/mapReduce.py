#%%
def square(x): return x * x
r = map(square, [1,2,3,4,5]) # 算子
print(list(r))

#%%
from functools import reduce
r = reduce(lambda x,y: x+y, [1,2,3,4,5])
r

#%%
# hash表面对太多对象，如云存储时，会改为使用不容/伦过滤器