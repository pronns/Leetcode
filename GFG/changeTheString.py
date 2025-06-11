"""
Input: s = "abCD"
Output: "abcd"
Explanation: The first letter (a) is lowercase. Hence, the complete string is made lowercase.


"""

s = 'abCD'

def modify(s):
    res = ''
    # code here
    if s[0].isupper():
        res= s[0] + s[1:].upper()
    else:
        res= s[0] + s[1:].lower()
    return res

print(modify(s))