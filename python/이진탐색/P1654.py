K,N = map(int,input().split())
ransun=[]
result=[]

for _ in range(K):
    ransun.append(int(input()))

left=1
right = int(pow(2,31))-1
mid=0
while left<=right:
    mid=(left+right)//2
    sum=0
    for value in ransun:
        sum+=value//mid
    if(sum<N):
        right=mid-1    
    elif(sum>=N):
        result.append({"count":sum,"length":mid})
        left=mid+1

max_idx=0
for i in range(len(result)):
    if(result[i]["count"]>result[max_idx]["count"] and result[i]["count"]>=N):
      continue
    elif(result[i]["count"]==result[max_idx]["count"]):
        if(result[i]["length"]>result[max_idx]["length"]):
            max_idx=i
    elif(result[i]["count"]<result[max_idx]["count"] and result[i]["count"]>=N):
        max_idx=i

print(result[max_idx]["length"])
