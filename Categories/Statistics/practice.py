#%%
# 利用马尔科夫链模拟自动文本生成
import random
def build_dict(filename):
    di = {}
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    prev = ''
    for word in words:
        if prev not in di:
            di[prev] = set([word])
        else:
            di[prev].add(word)
        prev = word
    for k,v in di.items():
        di[k]=list(v)
    return di

def write_doc(di, word):
    words=[word]
    for i in range(1,25):
        choices = di[word] if word in di else di['']
        word = random.choice(choices)
        words.append(word)
    print(' '.join(words))

di = build_dict('./Categories/Statistics/trade.txt')
#print(di)
write_doc(di, 'global')

#%%
# 给出整数流和窗口大小，计算华东窗口中所有整数的平均数
# MovingAverage m = new MovingAverage(3)
# m.next(1) = 1
# m.next(10) = (1+10)/2
# m.next(3) = (1+10+3)/3
# m.next(5) = (10+3+5)/3

class MovingAverage:
    """
    @params: size: An Integer
    """
    def __init(self, size):
        self.size = size
        self.queue = [0]*size
        self.start = 0
        self.size = 0 ....

#%%
# quickly gegerate array
[0]*5 + [1]*4
# for 2-dimensions array
a = [[0,0,0]]*3 # wrong
# a = [[0,0,0] for i in range(3)] # correct
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
a[1][1] = 100
print(a)

