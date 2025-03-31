def getSecondLargest(l):
    if len(l)<1:
        return None
    lar = l[0]
    slar = None
    for x in range(1,len(l)):
        if l[x]>lar:
            slar = lar 
            lar = l[x]
        elif l[x]!=lar:
            if slar==None or slar<l[x]:
                slar = l[x]
    return slar
    
l = [1,4,6,2,76,7,36]

print(getSecondLargest(l))