# two integer sum

## requirements

find two nums that can add up to a specific target

1. example 1
    nums = [2,7,11,14], target = 9
    return [0,1]

2. example 2
    nums = [2,7,11,15,4,23,19,5], target = 19
    return [3,4]

## solution

### brute force

1. time complexity
    O($n^2$)

### optimized

using differenciation
key is the dif amount, value is the position of the original counterpart

[2,7,...] target 9

7: 0
2: 1

1. time complexity
    O(n)

2. space complexity
    O(n)