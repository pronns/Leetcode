def searchInSorted(arr, k):
    #Your code here
    start , end = 0, len(arr)
    
    for i in range(start,end):
        mid = (start+end)//2
        if k > arr[mid]:
            start=mid
            continue
        elif k<arr[mid]:
            end=mid
            continue
        else:
            return True
    return False

print(searchInSorted([1,2,3,4,6],6))

