def twosum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic.keys():
            return [dic[nums[i]], i]
        else:
            dic[target - nums[i]] = i
    
    return []

print("nums = [2,7,11,14], target = 9", twosum([2,7,11,15], 9))
print("nums = [2,7,11,15,4,23,19,5], target = 19", twosum([2,7,11,15,4,23,19,5], 19))

