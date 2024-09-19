from collections import deque

N=int(input())
building=[]

for _ in range(N):
    building.append(list(map(int,input().split())))

result=[]

def bfs(copy_building,start,visited):
    dRow=[0,1,0,-1]
    dCol=[-1,0,1,0]
    queue=deque()
    queue.append(start)
    visited[start[0]][start[1]]=True
    while queue:
        ele = queue.popleft()
        for i in range(0,4):
            nRow=ele[0]+dRow[i]
            nCol=ele[1]+dCol[i]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>N-1):
                continue
            if(not visited[nRow][nCol] and copy_building[nRow][nCol]>0):
                queue.append([nRow,nCol])
                visited[nRow][nCol]=True
    

for rain in range(0,101):
    visited=[[False for _ in range(N)] for j in range(N)]
    count=0
    for row in range(N):
        for col in range(N):
            building[row][col]-=rain
    for row in range(N):
        for col in range(N):
            if(not visited[row][col] and building[row][col] > 0):
                count+=1
                bfs(building,[row,col],visited)
    for row in range(N):
        for col in range(N):
            building[row][col]+=rain
    result.append(count)
print(max(result))