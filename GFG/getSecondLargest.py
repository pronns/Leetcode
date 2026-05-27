"""
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.


"""

def getSecondLargest( arr):
        # Code Here
    maxi = max(arr)
    max2=float("-inf")
    for i, num in enumerate(arr):
        if num>max2 and num!=maxi:
            max2 = num
    if len(set(arr))==1:
        return -1
    return max2 