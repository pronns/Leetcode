def leftRotate(l):
    l = l[1:] + l[0:1]
    l.append(l.pop())
    print(l)

l = [10,20,40,56]

leftRotate(l)
l = [10,20,40,56]

def leftRotate(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    l[n-1] = x
    return l

print(leftRotate(l))
