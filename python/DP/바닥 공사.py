N = int(input())

DP=[0 for _ in range(N)]

DP[0]=1
DP[1]=3

for i in range(2,N):
    DP[i]=DP[i-2]*2+DP[i-1]%796796
    
print(DP)