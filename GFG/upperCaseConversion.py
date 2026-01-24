"""
Given a string s, convert the first letter of each word in the string to uppercase. 


Input: s = "i love programming"
Output: "I Love Programming"
"""
s = "i love programming"
def convert(s):
    # code here
    lst = s.split(" ")
    for i in range(len(lst)):
        word = lst[i]
        res = word[0].upper()+word[1:]
        lst[i] = res
    final_s= " ".join(lst)
    return final_s

print(convert(s))