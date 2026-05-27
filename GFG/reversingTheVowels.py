"""
Docstring for GFG.reversingTheVowels

Given a string consisting of lowercase English alphabets, reverse only the vowels present in it and print the resulting string.

Examples:

Input: s = "geeksforgeeks"
Output: "geeksforgeeks"
Explanation: The vowels are: e, e, o, e, e. Reverse of these is also e, e, o, e, e.
Input: s = "practice"
Output: "prectica"
Explanation: The vowels are a, i, e. Reverse of these is e, i, a.
Input: s = "bcdfg"
Output: "bcdfg"
Explanation: There are no vowels in s.
"""


def modify( s):
        # code here
    s = list(s)
    vowels = "aeiouAEIOU"
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return ''.join(s)

print(modify("practiced"))
