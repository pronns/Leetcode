"""Given an array of N positive integers where all numbers occur even number of times except one number which occurs odd number of times. Find the exceptional number.


N = 7
Arr[] = {1, 2, 3, 2, 3, 1, 3}
Output: 3
Explaination: 3 occurs three times.
"""


def getOddOccurrence(arr, n):
        # code here 
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] = 1+dic.get(arr[i])
        else:
            dic[arr[i]] = 1
        
    for key,val in dic.items():
        if val%2!=0:
            return key
    return -1

N = 7
Arr = {1, 2, 3, 2, 3, 1, 3}


print(getOddOccurrence(Arr,N))