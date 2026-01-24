"""Given a string S of lowercase alphabets, check if it is isogram or not. An Isogram is a string in which no letter occurs more than once.

Example 1:

Input:
S = machine
Output: 1
Explanation: machine is an isogram
as no letter has appeared twice. Hence
we print 1."""


def isIsogram(s):
        #Your code here
    dic = {}
    for char in s:
        if char in dic:
            return 0
        else:
            dic[char] = 1
    return 1

s = 'machine'
print(isIsogram(s))