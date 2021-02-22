def is_anagram(word1, word2):
    pass

def is_anagram_nlogn(word1, word2):
    return sorted(word1) == sorted(word2)

def is_anagram_n(word1, word2):
    if len(word1) != len(word2):
        return False

    # using two hashmaps
    dict1 = {}
    dict2 = {}

    for i in range(len(word1)):
        if word1[i] not in dict1.keys():
            dict1[word1[i]] = 1
        else:
            dict1[word1[i]] += 1
            
    for i in range(len(word2)):
        if word2[i] not in dict2.keys():
            dict1[word2[i]] = 1
        else:
            dict1[word2[i]] += 1
    
    for key, value in dict1.items():
        if dict2[key] != value:
            return False

    return True
print("O(nlogn) is_anagram for abc & cba: ", is_anagram_nlogn("abc", "cba"))
print("O(n) is_anagram for abc & cba: ", is_anagram_nlogn("abc", "cba"))

print("O(nlogn) is_anagram for cinema & iceman: ", is_anagram_nlogn("cinema", "iceman"))
print("O(n) is_anagram for cinema & iceman: ", is_anagram_nlogn("cinema", "iceman"))

print("O(nlogn) is_anagram for bumblebee & iceman: ", is_anagram_nlogn("bumblebee", "iceman"))
print("O(n) is_anagram for bumblebee & iceman: ", is_anagram_nlogn("bumblebee", "iceman"))
