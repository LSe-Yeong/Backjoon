array=list(map(int,input()))

result = array[0]
for i in range(1,len(array)):
    if array[i] <= 1 or result<=1:
        result = result + array[i]
    else:
        result = result * array[i]

print(result)