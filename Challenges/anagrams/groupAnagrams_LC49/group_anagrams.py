import collections

def group_anagrams_reassign_array(strs):
    dic = {}

    for i in range(len(strs)):
        sorted_anagram = "".join(sorted(strs[i]))
        group_strs = dic.get(sorted_anagram, [])
        group_strs.append(strs[i])
        dic[sorted_anagram] = group_strs

    return list(dic.values())

def group_anagrams_append_array(strs):
    dic = collections.defaultdict(list)

    for i in range(len(strs)):
        sorted_anagram = "".join(sorted(strs[i]))

        dic[sorted_anagram].append(strs[i])

    first_return_array = list(dic.values())
    for arr in first_return_array:
        arr.sort()
    first_return_array.sort(key=len,reverse=True)
    return first_return_array

print('["eat","tea","tan","ate","nat","bat","ad","da"] for group_anagrams_reassign_array: ', group_anagrams_reassign_array(["eat", "tea", "tan", "ate", "nat", "bat","ad" ,"da"]))
print('["eat","tea","tan","ate","nat","bat","ad","da"] for group_anagrams_append_array: ', group_anagrams_append_array(["eat", "tea", "tan", "ate", "nat", "bat","ad" ,"da"]))
