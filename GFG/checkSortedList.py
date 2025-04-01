def isSorted(l):
    i = 1
    while i<len(l):
        if l[i]< l[i-1]:
            return False
        i+=1
    return True

l = [10,20,30,40]
print(isSorted(l))


#using sorted function -> sort changes the same list, sorted creates a new copy of the list
def isSorted(l):
    s1 = sorted(l)
    if s1==l:
        return True
    else:
        return False
    
l = [10,20,30,40]
print(isSorted(l))