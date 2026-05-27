"""
Given an integer k and array arr. Your task is to return the position of the first occurrence of k in the given array and if element k is not present in the array then return -1.

Note: 1-based indexing is followed here.

Examples:

Input: k = 16 , arr = [9, 7, 16, 16, 4]
Output: 3
Explanation: The value 16 is found in the given array at positions 3 and 4, with position 3 being the first occurrence.


"""

k = 16 
arr = [9, 7, 16, 16, 4]
def search( k, arr) :
        # code here
    for i,n in enumerate(arr):
        if k==n:
            return i+1
    return -1

print(search(k,arr))
