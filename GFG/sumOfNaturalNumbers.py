def seriesSum(n : int) -> int:
    # code here
    res = 0
    if n==0:
        return res
    for i in range(n+1):
        res+=i
    return res

print(seriesSum(5))