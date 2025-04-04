def removeDups(arr,n):
    temp = [0]*n
    temp[0] = arr[0]
    res = 1
    for i in range(1,n):
        if temp[res-1]!=arr[i]:
            temp[res] = arr[i]
            res+=1
    for i in range(0,res):
        arr[i]= temp[i]
    return res