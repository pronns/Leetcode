"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

nums = [5,4,-1,7,8]
nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    maxSub = nums[0]
    curSum = 0

    for num in nums:
        if curSum<0:
            curSum = 0
        curSum+=num
        maxSub = max(maxSub,curSum)
    return maxSub

print(maxSubArray(nums))

#strategy: use sliding window, if curSum < 0 , make curSum=0 and add num to curSum, take max of maxSub and curSum