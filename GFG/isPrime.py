def isPrime(n):
        # code here
    if n==1:
        return False
    
    for num in range(2,n//2):
        if n%num==0:
            return False
    return True

print(isPrime(13))


"""check only till n/2 -> after n/2 no need to check"""