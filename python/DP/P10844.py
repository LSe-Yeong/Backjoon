N=int(input())

dp=[[0 for _ in range(10)] for k in range(N)]

A=[0,1,1,1,1,1,1,1,1,1]

for i in range(10):
    dp[0][i]=A[i]

for i in range(1,N):
    for k in range(10):
        if(k==0):
            dp[i][k]=dp[i-1][1]
        elif(k==9):
            dp[i][k]=dp[i-1][8]
        else:
            dp[i][k]=dp[i-1][k-1]+dp[i-1][k+1]

print(sum(dp[-1])%1000000000)
