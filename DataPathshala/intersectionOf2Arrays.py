from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        result = []
        for num in nums1:
            dic[num] = dic.get(num, 0) + 1
        
        for num in nums2:
            if num in dic and dic[num] > 0:
                result.append(num)
                dic[num] -= 1  
        return result
    
solution = Solution()
result = solution.intersection([4, 9, 5], [9, 4, 9, 8, 4])
print(result)