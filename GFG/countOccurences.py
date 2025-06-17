arr = [1, 2, 2, 3, 1, 4, 5, 1]

def count_occurrences(arr):
    maps = {}
    for num in arr:
        maps[num]=1 + maps.get(num,0)
    return maps

print(count_occurrences(arr))