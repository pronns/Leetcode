"""
Remove common characters and concatenate
Difficulty: BasicAccuracy: 30.78%Submissions: 77K+Points: 1Average Time: 30m
Given two strings, s1 and s2. The task is to remove all characters that are common in both strings and then combine the remaining characters from each string to form a new string. The characters that are not shared between the two strings should appear in the result in the same order as they appear in their respective original strings. If, after removing the common characters, no characters are left to form the result, return "-1"

Examples:

Input: s1 = aacdb, s2 = gafd
Output: cbgf
Explanation: The common characters of s1 and s2 are: a, d. The uncommon characters of s1 and s2 are c, b, g and f. Thus the modified string with uncommon characters concatenated is cbgf.
Input: s1 = abcs, s2 = cxzca
Output: bsxz
Explanation: The common characters of s1 and s2 are: a,c. The uncommon characters of s1 and s2 are b,s,x and z. Thus the modified string with uncommon characters concatenated is bsxz.

"""

s1 = "aacdb"
s2 = "gafd"

def concatenatedString(s1,s2):
    str=""
    flag=0
    for char in s1:
        if char in s2:
            continue
        else:
            flag=1
            str+=char
            
    for char in s2:
        if char in s1:
            continue
        else:
            flag=1
            str+=char
            
    if flag==0:
        return -1
    else:
        return str
    
print(concatenatedString(s1,s2))

##alternate solution using dict

def concatenatedString(s1,s2):
        #code here
    res = []
    dict1, dict2 = {}, {}
    for char in s1:
        if char in dict1:
            dict1[char]+=1
        else:
            dict1[char]=1
    for char in s2:
        if char in dict2:
            dict2[char]+=1
        else:
            dict2[char]=1
    for char in s1:
        if char not in dict2:   
            res.append(char)
    for char in s2:
        if char not in dict1:   
            res.append(char)
    s="".join(res)
    return s if s else -1