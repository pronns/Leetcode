def get_min_max( arr):
    min = float('inf')
    max = float('-inf')
    
    for i in range(len(arr)):
        if arr[i]>max:
            max = arr[i]
        if arr[i]<min:
            min = arr[i]
    return min, max

arr = [1, 345, 234, 21, 56789]

print(get_min_max(arr))