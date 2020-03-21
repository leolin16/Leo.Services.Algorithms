# anagrams

## requirements

### IsAnagram

1. "abc" "cba" -> True
2. "cinema" "iceman" -> True
3. "bumblebee "icecream" -> False

## solution

### sorting

#### time complexity

O($nlogn$)

#### code

```python
def is_anagram_nlogn(word1, word2):
    return sorted(word1) == sorted(word2)
```

### optimized

#### time complexity

O(n)

#### space complexity

O(n)

#### code

```python
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
```
