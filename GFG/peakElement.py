"""
def peakElement(self,arr):
        # Code here
        arr.insert(0,float('-inf'))
        arr.append(float('-inf'))
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                return i
        return 0


Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
"""


arr = [1, 2, 4, 5, 7, 8, 3]
def peakElement(arr):
    # Code here
    arr.insert(0,float('-inf'))
    arr.append(float('-inf'))
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            return i
    return 0

print(peakElement(arr))