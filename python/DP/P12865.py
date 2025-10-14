# N,K = map(int,input().split())
# w=[]
# v=[]

# DP=[[0 for _ in range(K+1)] for i in range(N+1)]

# for i in range(N):
#     weight, value = map(int,input().split())
#     w.append(weight)
#     v.append(value)

# for i in range(1,N+1):
#     for j in range(K+1):
#         if j<w[i-1]:
#             DP[i][j]=DP[i-1][j]
#         else:
#             DP[i][j]=max(DP[i-1][j],DP[i-1][j-w[i-1]]+v[i-1])

# print(DP[N][K])

def NS(n,k):
    if k < 0:
        return 
    if n==0:
        DP[n][k] = 0
        return DP[n][k]
    if DP[n][k] != -1:
        return DP[n][k]

    ns1 = NS(n-1,k)
    ns2 = NS(n-1,k-items[n-1][0])
    if ns2 is not None:
        DP[n][k] = max(ns1,ns2+items[n-1][1])
    else:
        DP[n][k] = ns1

    return DP[n][k]
    
N, K =map(int,input().split())
items = []
DP = [[-1 for i in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    w,v = map(int,input().split())
    items.append([w,v])

NS(N,K)

print(DP[N][K])


