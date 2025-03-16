"""
217.Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

"""

#my solution
nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3]
nums = [2,14,18,22,22]
def containsDuplicate(nums):
    maps = {}
    for num in nums:
        maps[num] = 1 + maps.get(num,0)
    for key,val in maps.items():
        if val>1:
            return True
    return False
    
print(containsDuplicate(nums))


#best sol - use hashset
def containsDuplicate(nums):
    mapsset = set()
    for num in nums:
        if num in mapsset:
            return True
        else:
            mapsset.add(num)

print(containsDuplicate(nums))