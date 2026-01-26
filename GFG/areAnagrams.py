""""
Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

Examples:

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams.
Input: s1 = "allergy", s2 = "allergyy" 
Output: false 
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams. 
Input: s1 = "listen", s2 = "lists" 
Output: false 
Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.
"""


def areAnagrams( s1, s2):
    # code here
    dict1 = {}
    dict2 = {}
    for char in s1:
        dict1[char] =1+dict1.get(char,0)
    for char in s2:
        dict2[char] =1+dict2.get(char,0)
    return dict1 == dict2

s1 ,s2 = "geeks" , "kseeg"
print(areAnagrams(s1,s2))