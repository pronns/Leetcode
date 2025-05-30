"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
 
"""

s= []
s.append("(")
print(s)
s.append("]")
print(s)
t = s.pop()
print(t)
print(s)

def isValid(s):
    stack = []
    maps = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in maps:
            if stack and stack[-1]==maps[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
s = "([])"
print(isValid(s))

