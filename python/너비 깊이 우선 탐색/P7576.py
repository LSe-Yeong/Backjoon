from collections import deque

queue=deque()

def bfs():
    dRow=[1,-1,0,0]
    dCol=[0,0,1,-1]
    visited=[[False for _ in range(col)] for k in range(row)]
    while queue:
        ele = queue.popleft()
        for i in range(4):
            nRow=ele[0]+dRow[i]
            nCol=ele[1]+dCol[i]
            if(nRow < 0 or nRow > row-1 or nCol < 0 or nCol >col-1):
                continue
            if(tomato[nRow][nCol]==0):
                visited[nRow][nCol]=True
                tomato[nRow][nCol]=tomato[ele[0]][ele[1]]+1
                queue.append([nRow,nCol])
                


col, row = map(int,input().split())

tomato = []
isEnd=True
isExist0 = False

for _ in range(row):
    tomato.append(list(map(int,input().split())))

for r in range(row):
    for c in range(col):
        if tomato[r][c]==1:
            queue.append([r,c])

bfs()

maxValue=0
for item in tomato:
    if 0 in item:
        print(-1)
        exit()
    if(maxValue<=max(item)):
        maxValue=max(item)
print(maxValue-1)
