from collections import deque

def bfs(start,R,C):
    queue=deque()
    dRow=[1,1,1,0,0,-1,-1,-1]
    dCol=[-1,0,1,1,-1,1,-1,0]
    queue.append(start)
    visited[start[0]][start[1]]=True
    while queue:
        ele = queue.popleft()
        row=ele[0]
        col=ele[1]
        for i in range(len(dRow)):
            nRow=row+dRow[i]
            nCol=col+dCol[i]
            if(nRow<0 or nRow>R-1 or nCol<0 or nCol>C-1):
                continue
            if(not visited[nRow][nCol] and my_map[nRow][nCol]==1):
                visited[nRow][nCol]=True
                queue.append([nRow,nCol])

while True:
    my_map=[]
    count=0
    col,row = map(int,input().split())
    visited=[[False for _ in range(col)] for k in range(row)]
    if(col == 0 and row ==0):
        break
    for _ in range(row):
        my_map.append(list(map(int,input().split())))
    for r in range(row):
        for c in range(col):
            if(not visited[r][c] and my_map[r][c]==1):
                count+=1
                bfs([r,c],row,col) 
    print(count)