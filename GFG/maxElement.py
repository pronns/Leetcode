def getMax(l):
    max = -99999999
    for i,num in enumerate(l):
        if num>max:
            max=num
    return max

l = [1,4,6,2,76,7,36]

print(getMax(l))