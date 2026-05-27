def delAlternate ( S):
        # code here 
    res = ''
    for i in range(len(S)):
        if (i)%2==0:
            res+=S[i]
    return res


"""
Given a string s as input. Delete the characters at odd indices of the string. Return the final string after deletion of characters at odd indices.

Examples :

Input: s = "Geeks"
Output: "Ges" 
Explanation: Deleted "e" at index 1 and "k" at index 3.
"""
S = "Geeks"
print(delAlternate(S))