def findLHS( nums) -> int:
        dic = {}
        for num in nums:
            dic[num] = 1+dic.get(num,0)
        
        maxi = 0
        for key,val in dic.items():
            if key+1 in dic:
                current_length = val+ dic[key+1]
                if current_length>maxi:
                    maxi = current_length
        return maxi

print(findLHS([1,3,2,2,5,2,3,7]))
