def count (s):
        # your code here
    uc, lc, num, sc = 0,0,0,0
    for char in s:
        if ord(char)>=65 and ord(char)<=90:
            uc+=1
        elif ord(char)>=97 and ord(char)<=122:
            lc+=1
        elif ord(char)>=48 and ord(char)<=57:
            num+=1
        else:
            sc+=1
    return uc,lc, num, sc
S = "#GeeKs01fOr@gEEks07"

print(count(S))