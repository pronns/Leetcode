arr = [1, 2, 3, 4, 5]


def countOddEven(arr):
    countE , countO = 0, 0

    for num in arr:
        if num%2==0:
            countE+=1
        else:
            countO+=1
    return countE, countO

print(countOddEven(arr))