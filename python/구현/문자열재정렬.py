array = input()

result=""
list_arr = list(array)
list_arr.sort()

idx=0
sum=0
while list_arr[idx]<"A":
    sum+=int(list_arr[idx])
    idx+=1

for i in range(idx,len(list_arr)):
    result+=list_arr[i]
result+=str(sum)

print(result)


