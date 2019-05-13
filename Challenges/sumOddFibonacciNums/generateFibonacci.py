#method1: regression
# 时间复杂度O（1.618^n）,而且最深度1000
def fib_recur(n):
  assert n >= 0, "n > 0"
  if n <= 1:
    return n
  return fib_recur(n-1) + fib_recur(n-2)

for i in range(1, 20):
    print(fib_recur(i), end=' ')

#method2: 递增
# 时间复杂度是 O(n)，呈线性增长
def fib_loop(n):
  a, b = 0, 1
  for i in range(n+1):
    a, b = b, a+b
    return a


for i in range(20):
  print(fib_loop(i), end=' ')

#method3: generator
def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a+b
        max -= 1
        yield a


for i in fib_loop_while(10):
    print(i)