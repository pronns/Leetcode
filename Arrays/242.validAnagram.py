"""
242.Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

"""

s = "anagram"
t = "nagaram"


def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    smap, tmap ={}, {}
    for i in range(len(s)):
        smap[s[i]] = 1+smap.get(s[i],0)
        tmap[t[i]] = 1+tmap.get(t[i],0)
    for c in smap:
        if smap[c]!=tmap.get(c,0):
            return False
    return True

print(isAnagram(s,t))