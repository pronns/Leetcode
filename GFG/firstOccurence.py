"""
Docstring for GFG.firstOccurence
Given two strings txt and pat, return the 0-based index of the first occurrence of the substring pat in txt. If pat is not found, return -1.
Note: You are not allowed to use the inbuilt function.

Examples :

Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1
Explanation: "Fr" is not present in the string "GeeksForGeeks" as substring.
Input: txt = "GeeksForGeeks", pat = "For"
Output: 5
Explanation: "For" is present as substring in "GeeksForGeeks" from index 5 (0 based indexing).
Input: txt = "GeeksForGeeks", pat = "gr"
Output: -1
Explanation: "gr" is not present in the string "GeeksForGeeks" as substring.
"""

def firstOccurence(txt,pat):
    #code here
    for i in range(len(txt)):
        val = txt[i]
        if pat[0]==val:
            a = txt[i:i+len(pat)]
            if a==pat:
                return i
        else:
            continue
    return -1

pat = "on"
txt="Pronnoy"

print(firstOccurence(txt,pat))
