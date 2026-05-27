"""
Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

NOTE - If there are no repeating characters return '#'.

Example 1:

Input:
S = "geeksforgeeks"
Output: g
Explanation: g, e, k and s are the repeating
characters. Out of these, g occurs first. 
"""

def firstRep( s):
    # code here
    dic = {}
    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char]+=1
    for key,val in dic.items():
        if val>1:
            return key
    return '#'
S = "geeksforgeeks"
print(firstRep(S))