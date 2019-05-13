# set 无法用下标索引，只能用for，但可以转
#%%
# to split into list array
s="abc,def,ghi"
l=s.split(',+')
l

#%%
urls=["https://muses.live/news", "https://leolin.studio/yesman"]

for url in urls:
    parts=url.split('://') # return a list
    prefix=parts[0]
    domain=parts[1].split('/')[0]
    print('://'.join([prefix, domain]))

#%%
# use lambda to define a function
f = lambda x,y: (x*y, x-y, x+y, x**y) # 元组是只读数组，def时，可以不加(),默认元组
print(type(f))
a,b,_,_=f(8,9)
a
b