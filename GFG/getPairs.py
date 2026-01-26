
"""
Docstring for GFG.getPairs
Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:

Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].
Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].
Expected Time Complexity: O(n log n)
Expected Auxiliary Space: O(n).

"""


def getPairs(arr):
        # code here
    dict = {}
    res = []
    
    for num in arr:
        dict[num] = 1 + dict.get(num, 0)
    
    # Use a set to track processed keys
    processed = set()
    for key in dict.keys():
        if key in processed:
            continue
        if key == 0 and dict[key] > 1:
            res.append([0, 0])
        elif key != 0 and -key in dict:
            res.append([min(key, -key), max(key, -key)])
        # Mark both key and -key as processed
        processed.add(key)
        processed.add(-key)
    
    # Sort the result list
    res.sort()
    return res


print(getPairs([-1, 0, 1, 2, -1, -4]))

arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
print(getPairs(arr))
arr = [6, 10, -6, 10, 4, -9, -1, -10, -6, -5, 0 , 0 , 0]

print(getPairs(arr))