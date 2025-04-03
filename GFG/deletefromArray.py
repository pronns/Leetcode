"""
You are given an array arr(0-based indexing). The size of the array is given by n. You need to delete an element at given index and modify given array. The arr[i] of array is initially set to i+1.
Deletion means you need to shift all the elements after that index to the left by 1 position and set the last element as zero.

Example 1:

Input:
n = 5
index = 0
Output: 
2 3 4 5 0
Example 2:

Input:
n = 6
index = 3
Output: 
1 2 3 5 6 0
"""

def deleteFromArray(arr,n,idx):
    #code here
    arr[idx] = 0
    for i in range(idx,n-1):
        arr[i] =arr[i+1]
    arr[n-1]=0
    return arr

arr = [1,2,3,4,5]
n = 5
idx = 0

arr = [1,2,3,4,5,6]
n = 6
idx = 3

print(deleteFromArray(arr,n,idx))