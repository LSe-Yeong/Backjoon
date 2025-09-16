array=list(map(int,input()))

result = array[0]
for i in range(1,len(array)):
    if array[i] <= 1 or result<=1:
        result = result + array[i]
    else:
        result = result * array[i]

print(result)


str_num = input()
num = int(str_num[0])
for i in range(1,len(str_num)):
    if num<=1 or int(str_num) <=1:
        num = num + int(str_num[i]) 
    else:
        num = num * int(str_num[i])

print(num)