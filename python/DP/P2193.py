N = int(input())

DP=[0 for _ in range(N)]

if(N==1 or N==2):
    print(1)
else:
    DP[0]=1
    DP[1]=1
    for i in range(2,N):
        DP[i] = DP[i-2] + DP[i-1]
    print(DP[N-1])