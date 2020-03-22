# length of longest non-repeating sub string

## requirement

Given a string, return the length of the longest substring without repeating characters.

Example

1. lengthOfLongestSubstring("abcabcbb") --> 3 since length of "abc"
2. lengthOfLongestSubstring("bbbbb") --> 1 since length of "b"

## solution

### using sliding window technique

1. time complexity: O(n)
2. space complexity: O(min(m,n)) # m: size of the charset/alphabet, n: size of the string
