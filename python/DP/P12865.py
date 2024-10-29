N,K = map(int,input().split())
w=[]
v=[]

DP=[[0 for _ in range(K+1)] for i in range(N+1)]

for i in range(N):
    weight, value = map(int,input().split())
    w.append(weight)
    v.append(value)

for i in range(1,N+1):
    for j in range(K+1):
        if j<w[i-1]:
            DP[i][j]=DP[i-1][j]
        else:
            DP[i][j]=max(DP[i-1][j],DP[i-1][j-w[i-1]]+v[i-1])

print(DP[N][K])

