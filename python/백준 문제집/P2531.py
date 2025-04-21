N,D,K,C = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

left=0
result=[]

while (left<=len(arr)-1):
    subList = []
    for i in range(K):
        subList.append(arr[(left+i)%N])
    left+=1
    sushi_set = set(subList)
    if C in sushi_set:
        result.append(len(sushi_set))
    else:
        result.append(len(sushi_set)+1)

print(max(result))


    

