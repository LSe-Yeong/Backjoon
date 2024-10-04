import sys

N=int(input())
M=int(input())

INF=sys.maxsize

dist=[[INF for _ in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        if i==j:
            dist[i][j]=0

for i in range(M):
    row,col,value=map(int,input().split())
    if(dist[row-1][col-1]>value):
        dist[row-1][col-1]=value

for k in range(0,N):
    for row in range(0,N):
        for col in range(0,N):
            if(dist[row][col] > dist[row][k] + dist[k][col]):
                dist[row][col] =dist[row][k] + dist[k][col]

for row in range(N):
    for col in range(N):
        if(dist[row][col]==INF):
            dist[row][col]=0

for row in range(N):
    for col in range(N):
        print(dist[row][col], end=" ")
    print()    

