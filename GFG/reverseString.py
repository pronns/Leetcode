def revStr (s : str) -> str :
    # code here 
    res = ''
    for i in range(len(s)):
        res+=s[len(s)-i-1]
    return res
s = "GeeksforGeeks"
print(revStr(s))



"""Two pointer technique"""
def revStr(s: str) -> str:
    chars = list(s)
        
        # Initialize two pointers
    left = 0
    right = len(chars) - 1
    
    # Swap characters until pointers meet in the middle
    while left < right:
        # Swap characters at left and right pointers
        chars[left], chars[right] = chars[right], chars[left]
        # Move pointers toward each other
        left += 1
        right -= 1
    
    # Convert list back to string and return
    return ''.join(chars)