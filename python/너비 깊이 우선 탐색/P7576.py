from collections import deque

def bfs(start):
    queue=deque()
    dRow=[1,-1,0,0]
    dCol=[0,0,1,-1]
    visited=[[False for _ in range(col)] for k in range(row)]
    visited[start[0]][start[1]]=True
    queue.append(start)
    while queue:
        ele = queue.popleft()
        for i in range(4):
            nRow=ele[0]+dRow[i]
            nCol=ele[1]+dCol[i]
            if(nRow < 0 or nRow > row-1 or nCol < 0 or nCol >col-1):
                continue
            if(tomato[nRow][nCol]==0 and not visited[nRow][nCol]):
                visited[nRow][nCol]=True
                queue.append([nRow,nCol])
                if(distance[nRow][nCol]!=0):
                    distance[nRow][nCol]=min(distance[nRow][nCol],distance[ele[0]][ele[1]]+1)
                else:
                    distance[nRow][nCol]=distance[ele[0]][ele[1]]+1


col, row = map(int,input().split())

tomato = []
isEnd=True
isExist0 = False
distance=[[0 for _ in range(col)] for k in range(row)]

for _ in range(row):
    tomato.append(list(map(int,input().split())))

for r in range(row):
    for c in range(col):
        if(tomato[r][c]==-1):
            distance[r][c]=-1
        if(tomato[r][c]==1):
            distance[r][c]=1

for i in tomato:
    if 0 in i:
        isEnd=False
        break
    
if(not isEnd):
    for r in range(row):
        for c in range(col):
            if(tomato[r][c]==1):
                bfs([r,c])
    maxValue=0
    for item in distance:
        if 0 in item:
            isExist0 =True
            print(-1)
            break
        if(max(item)>=maxValue):
            maxValue=max(item)
    if(not isExist0):
        print(maxValue-1)
else:
    print(0)
