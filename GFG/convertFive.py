def convertFive(n):
    res = ''
    str_n = str(n)
    for char in str_n:
        if char == '0':
            res += '5'
        else:
            res += char
    return res

print(convertFive(1004))

