N= int(input())
M= int(input())

INF = 10e15

city = [[INF for _ in range(N+1)] for i in range(N+1)]

for _ in range(M):
    a,b,v=map(int,input().split())
    if(city[a][b]>v):
        city[a][b]=v

for r in range(1,N+1):
    city[r][r] = 0

for k in range(1,N+1):
    for r in range(1,N+1):
        for c in range(1,N+1):
            city[r][c] = min(city[r][c],city[r][k]+city[k][c])

for r in range(1,N+1):
    for c in range(1,N+1):
        if(city[r][c]==INF):
            print(0, end=" ")
        else:
            print(city[r][c],end=" ")
    print()
