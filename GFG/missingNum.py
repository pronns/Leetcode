#uses n square time complexity

def missingNum( arr):
    # code here
    length = len(arr)
    arr2 = []
    for num in range(length+1):
        arr2.append(num+1)
    for i in range(len(arr2)):
        if arr2[i] not in arr:
            return arr2[i]
    

print(missingNum([1,3,4,5]))

#uses O(n)

#use sum of array and sum of n elements -> subtract sum of n elements with sum of array


def missingNum( arr):
        # code here
    length = len(arr)+1
    sum2 = length* (length+1)//2
    sum1 = 0
    for i in range(len(arr)):
        sum1+=arr[i]
    return sum2-sum1
    
print(missingNum([1,3,4,5]))
