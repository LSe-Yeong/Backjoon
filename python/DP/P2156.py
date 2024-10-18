N=int(input())
grape=[0]*10000
for i in range(N):
    grape[i]=int(input())

DP=[0] *10000
answer=0

DP[0]=grape[0]
DP[1]=grape[1]+grape[0]
DP[2]=max(grape[0]+grape[2],grape[1]+grape[2],DP[1])

for i in range(3,N):
    DP[i]=max(DP[i-3]+grape[i-1]+grape[i],DP[i-2]+grape[i],DP[i-1])

print(max(DP))