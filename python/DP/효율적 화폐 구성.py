N,M = map(int,input().split())
values = []

for _ in range(N):
    values.append(int(input()))

DP = [0] * 10001

for v in values:
    DP[v]=1

values.sort()

for i in range(values[0],M+1):
    if(DP[i]!=0):
        continue
    DP[i]=1000000
    for v in values:
        if(DP[i-v]!=0):
            DP[i] = min(DP[i],DP[i-v])
    DP[i]+=1

if(DP[M]==1000001):
    print(-1)
else:
    print(DP[M])
    