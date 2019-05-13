#%%
def myrange(start, end, steps=1):
    i = start
    while i < end:
        yield i
        i += steps
    return 'done'

# print(type(myrange))
# for i in myrange(10,20,3):
#     print(i)

f = myrange(10,20,3)
try:
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
except Exception as e:
    print(type(e))
    print(str(e))

#%%
# 文件操作
def readlines(f):
    line = f.readline()
    while line:
        yield line.strip()
        line = f.readline()

# f = open('trade.txt', 'r')
# try:
#     for line in readlines(f):
#         print(line)
# except:
#     pass
# finally:
#     if f:
#         f.close()

with open('./Categories/Statistics/trade.txt', 'r') as f:
    for line in readlines(f):
        print(line)