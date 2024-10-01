N=int(input())
A=[0]
dp=[0 for _ in range(N+1)]

for _ in range(N):
    A.append(int(input()))

if(N==1):
    print(A[1])
elif(N==2):
    print(A[1]+A[2])
else:
    dp[1]=A[1]
    dp[2]=A[1]+A[2]
    dp[3]=max(A[2]+A[3],A[1]+A[3])

    for i in range(4,N+1):
        dp[i] = max(dp[i-3]+A[i-1]+A[i],dp[i-2]+A[i])

    print(dp[N])