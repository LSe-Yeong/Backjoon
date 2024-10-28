N=int(input())

DP=[0 for i in range(N)]

if N==1:
    print(1)
elif N==2:
    print(3)
else:
    DP[0]=1
    DP[1]=3

    for i in range(2,N):
        DP[i]=(DP[i-2]*2+DP[i-1])%10007

    print(DP[N-1])