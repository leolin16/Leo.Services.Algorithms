#%%
def array_from_file(file_path):
    fi = open(file_path, mode='r')
    temp_str = fi.read().strip().replace('\n',',').replace(' ','').strip(',')
    fi.close()
    return temp_str

#%%
import collections

def group_anagrams_reassign_array(strs:list):
    dic = {}

    for i in range(len(strs)):
        sorted_anagram = "".join(sorted(strs[i]))
        group_strs = dic.get(sorted_anagram, [])
        group_strs.append(strs[i])
        dic[sorted_anagram] = group_strs

    return list(dic.values())

def group_anagrams_append_array(strs):
    dic = {}

    for i in range(len(strs)):
        sorted_anagram = "".join(sorted(strs[i]))
        if sorted_anagram not in dic:
            dic[sorted_anagram] = [strs[i]]
        else:
            dic[sorted_anagram].append(strs[i])

    return list(dic.values())

def group_anagrams_append_array_set_collection(strs):
    dic = collections.defaultdict(list)

    for i in range(len(strs)):
        sorted_anagram = "".join(sorted(set(strs[i])))[0:3]

        dic[sorted_anagram].append(strs[i])

    first_return_array = list(dic.values())
    for arr in first_return_array:
        arr.sort()
    first_return_array.sort(key=len,reverse=False)
    return first_return_array



#%%

import os
os.chdir('c:/Projects/Leo.Services.Algorithms/Challenges/anagrams')
temp_path = os.path.join(os.getcwd(),'groupAnagrams_LC49','anagrams_data1.txt')
print(temp_path)
origin_str = array_from_file(temp_path)
print(origin_str)
str_arr = origin_str.split(',')
print("array string is: ", str_arr)

print('["eat","tea","tan","ate","nat","bat","ad","da"] for group_anagrams_reassign_array: ', group_anagrams_reassign_array(["eat", "tea", "tan", "ate", "nat", "bat","ad" ,"da"]))
print('["eat","tea","tan","ate","nat","bat","ad","da"] for group_anagrams_append_array: ', group_anagrams_append_array(["eat", "tea", "tan", "ate", "nat", "bat","ad" ,"da"]))
print("['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'ear', 'abcsa', 'cat', 'tac', 'era', 'abc', 'abcs', 'abcssab'] for group_anagrams_append_array: ", group_anagrams_append_array(['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'ear', 'abcsa', 'cat', 'tac', 'era', 'abc', 'abcs', 'abcssab']))

# %%
print(sorted(set('google')))

# %%
