def nonRepeatingChar(s):
    #code here
    dic = {}
    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] +=1
            
    for key,val in dic.items():
        if val==1:
            return key
    return -1
s = "geeksforgeeks"
print(nonRepeatingChar(s))