N = int(input())

INF = 10e9
my_map = []
dist = [[INF for _ in range(N)] for i in range(N)]

for _ in range(N):
    my_map.append(list(map(int,input().split())))
    
for row in range(N):
    for col in range(N):
        if(my_map[row][col]==1):
            dist[row][col]=1
            
for k in range(N):
    for r in range(N):
        for c in range(N):
            if(dist[r][k]+dist[k][c]<dist[r][c]):
                dist[r][c]=dist[r][k]+dist[k][c]

for r in range(N):
    for c in range(N):
        if(dist[r][c]==INF):
            dist[r][c]=0
        else:
            dist[r][c]=1

for r in range(N):
    for c in range(N):
        print(dist[r][c],end=" ")
    print()