N = int(input())
A = list(map(int,input().split()))
DP = [0 for _ in range(N)]

DP[0]=A[0]
DP[1]=max(A[0],A[1])

for i in range(2,N):
    DP[i]=max(DP[i-1],DP[i-2]+A[i]) 

print(DP[N-1])