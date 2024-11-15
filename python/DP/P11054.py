N = int(input())
array = list(map(int,input().split()))
reverse_array = array[::-1]

DP=[0 for _ in range(N)]
subDP=[0 for _ in range(N)]

DP[0]=1
subDP[0]=1

for i in range(1,N):
    DP[i]=1
    subDP[i]=1
    for j in range(0,i):
        if(array[j]<array[i] and DP[j]+1>DP[i]):
            DP[i]=DP[j]+1
        if(reverse_array[j]<reverse_array[i] and subDP[j]+1>subDP[i]):
            subDP[i]=subDP[j]+1

subDP=subDP[::-1]

max_value=0
for i in range(len(DP)):
    if(DP[i]+subDP[i]>max_value):
        max_value=DP[i]+subDP[i]

print(max_value-1)

  