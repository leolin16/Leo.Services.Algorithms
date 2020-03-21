def is_anagram(word1, word2):
    pass

def is_anagram_nlogn(word1, word2):
    return sorted(word1) == sorted(word2)

print(is_anagram_nlogn("abc", "cba"))