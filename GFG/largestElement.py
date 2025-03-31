#get max element in list

def getMax(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i]>res:
                res = l[i]
        return res
    
l = [1,4,6,2,76,7,36]

print(getMax(l))