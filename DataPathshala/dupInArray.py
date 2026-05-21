from typing import List

def findDuplicate( nums: List[int]) -> int:
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return nums[i]
        else:
            dic[nums[i]] = 1+dic.get(nums[i],0)

print(findDuplicate([3,1,3,4,2]))