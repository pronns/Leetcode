"""
Docstring for GFG.runLengthEncoding
Given a string s, Your task is to complete the function encode that returns the run length encoded string for the given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded and returns the encoded string.

Example 1:

Input:
s = aaaabbbccc
Output: a4b3c3
Explanation: a repeated 4 times consecutively b 3 times, c also 3 times.
Example 2:

Input:
s = abbbcdddd
Output: a1b3c1d4
Explanation:  a repeated 1 time, b 3 times, c 1 time and d repeated 4 times.



"""


def encode( s ):
        # code here
    lst = []
    cnt =1
    #lst.append(s[0])
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            lst.append(s[i-1])
            lst.append(cnt)
            cnt = 1
        else:
            cnt+=1
    lst.append(s[-1])
    lst.append(cnt)
    final = ''.join(map(str,lst))
    return final

print(encode('eaaaabbbbccccdd'))