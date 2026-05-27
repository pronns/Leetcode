arr = [1,2,3,4,5,6]
output = []

for i in range(len(arr)):
    if i%2==0:
        output.append(arr[i])
    else:
        continue
        
print(output)