from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    lst = []
    i = 0
    
    while i < len(nums):
        start = nums[i] 
        while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            i += 1
        end = nums[i]
        if start == end:
            lst.append(str(start))
        else:
            lst.append(f"{start}->{end}")
            i += 1
        
    return lst