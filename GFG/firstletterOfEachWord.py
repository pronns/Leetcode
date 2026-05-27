def firstAlphabet( S):
		# code here
    lst = S.split(" ")
    lst2 = []
    for char in lst:
        lst2.append(char[0])
        continue
    return ''.join(lst2)

print(firstAlphabet("Geeks For Geeks"))