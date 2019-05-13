#%%
def f(x,y): return x+y

# delay calculation
def high_f(f,x,y):
    def wrapper():
        return f(x,y)
    return wrapper

# fix some parameters
def partial_f(f,x):
    def wrapper(y):
        return f(x,y)
    return wrapper

f1 = high_f(f, 100, 200)
f2 = high_f(f, 200, 300)

print(f1())
print(f2())

fp1 = partial_f(f, 200)
print(fp1(300))
print(fp1(500))

#%%
# decorator
def log(f):
    def wrapper(*args, **kws):
        '''
        print('log %s' % f.__name__)
        return f(*args, **kws)
        '''
        r = f(*args, **kws)
        print('log %s' % f.__name__)
        return r
    return wrapper

@log
def fadd(x,y): return x+y
@log
def fmul(x,y): return x*y
# log_fadd = log(fadd)
print(fadd(100,200))
print(fmul(100,200))

#%%
# 动态调整类的实例
class MyClass:
    def __init__(self, x,y):
        self.x=x
        self.y=y
a=MyClass(1,2)
b=MyClass(3,4)
a.z=100 #动态添加属性
print(a.x,a.y,a.z)
# print(b.z) # should reporting error
print(getattr(b,'z','zzz')) # will return default, here zzz, if attribute doesn't exist
setattr(b,'z','xxx')
print(b.z)