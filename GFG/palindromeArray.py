import copy
from typing import List


def isPerfect( arr : List[int]) -> bool:
    # code here
    arr1=copy.deepcopy(arr)
    i = 0
    j = len(arr)-1
    while i<j:
        arr1[i],arr1[j] = arr1[j],arr1[i]
        i+=1
        j-=1
    if arr == arr1:
        return True
    return False
    
print(isPerfect([1,2,3,2,1]))