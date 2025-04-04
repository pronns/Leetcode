def reverseList(l):
    #l.reverse()
    new_l = list(reversed(l))
    new_l2 = l[::-1]
    print(new_l)
    print(new_l2)

l = [10,20,40,52,98]

reverseList(l)


#using custom method

#use two pointers, one from start, one from end. and swap

def reverseList(l):
    s = 0
    e = len(l)-1
    while s<e:
        l[s], l[e] = l[e] , l[s]
        s+=1
        e-=1
    return l

print(reverseList(l))