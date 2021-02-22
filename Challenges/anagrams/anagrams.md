# anagrams

## requirements

### IsAnagram

1. "abc" "cba" -> True
2. "cinema" "iceman" -> True
3. "bumblebee "icecream" -> False

### GroupAnagrams

1. Input ["eat","tea","tan","ate","nat","bat"]
2. Output [["ate","eat","tea"],["nat","tan"],["bat"]]

## solution

### sorting

1. time complexity

    O($nlogn$) for comparing 2
    O($n * mlogm$) for grouping anagrams


### optimized

needs hashmaps

1. time complexity

    O(n) for comparing 2
    O(n * m) for grouping anagrams, needs prime factorizations for each letter

2. space complexity

    O(n) for comparing 2

