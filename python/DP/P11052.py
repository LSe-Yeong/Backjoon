N = int(input())
card=list(map(int,input().split()))
card.insert(0,0)
DP=[0 for _ in range(N+1)]

DP[1]=card[1]

for i in range(2,N+1):
    DP[i]=card[i]
    for j in range(1,i):
        if(DP[i]<DP[j]+card[i-j]):
            DP[i]=DP[j]+card[i-j]

print(DP[N])
            