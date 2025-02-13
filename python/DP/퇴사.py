N = int(input())
array=[]

for _ in range(N):
    array.append(list(map(int,input().split())))

DP=[0 for _ in range(N)]

for i in range(N-1,-1,-1):
    if(i+array[i][0]==N):
        DP[i] = array[i][1]
        continue
    if(i+array[i][0]>N-1):
        continue
    DP[i] = max(DP[i+array[i][0]:N]) + array[i][1]

print(max(DP))
