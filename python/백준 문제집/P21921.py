N,X = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
right = X-1
sum = sum(arr[left:right+1])
left+=1
right+=1
result = [sum]

flag=True
for v in arr:
    if(v!=0):
        flag=False

if(flag):
    print("SAD")
else:
    while right<=len(arr)-1:
        sum = sum - arr[left-1]+arr[right]
        result.append(sum)
        left+=1
        right+=1
    max_value = max(result)
    print(max_value)
    print(result.count(max_value))




