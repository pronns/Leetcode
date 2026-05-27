from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    lst = []
    for i in range(1,len(nums)+1):
        if i not in nums:
            lst.append(i)
    return lst

#print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))