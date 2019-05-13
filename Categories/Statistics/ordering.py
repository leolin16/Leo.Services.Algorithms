# 给定一个字符串数组，x开头的在数组前部排序，非x开头的在后部排序
# 可以使用startswith, append, sorted, 复杂度过高，需要额外空间
# 快速排序，
# 修改字符串中字符时， 因为字符串本身不可改变，所以需要转成list再join

#%%
def sort_words(words):
    start = 0
    end = len(words) - 1
    while start < end:
        while (start < end) and words[start].startswith('x'):
            start += 1
        while (start < end) and (not words[end].startswith('x')):
            end -= 1
        if start < end:
            words[start], words[end] = words[end], words[start]

words_1 = ["xy", "yx", "abc", "def", "xabc", "dabc"]
sort_words(words_1)
print(words_1)

#%%
# 给定一个数组，每个元素是一个元组，按照每个元组最后一个元素进行排序
# 使用设计模式之策略模式
def sort_last(tuples):
    return sorted(tuples, key=lambda t: t[-1])

tuples_1 = [(1,2,3), (2,3,4), (0,1,2)]
sort_last(tuples_1)
tuples_1

#%%
# 合并两个已排序数组并重新排序
def linear_merge(li1, li2):
    result = []
    while len(li1) and len(li2):
        if li1[0] <= li2[0]:
            result.append(li1.pop(0))
        else:
            result.append(li2.pop(0))
    result.extend(li1)
    result.extend(li2)
    return result
mergedResult = linear_merge([1,2,3,5,6], [2,4,5,7,9,10])
mergedResult