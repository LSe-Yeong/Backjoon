from collections import deque

def bfs(start):
    queue=deque()
    dRow=[0,-1,0,1]
    dCol=[1,0,-1,0]
    row,col=start
    
    visited[row][col]=True
    queue.append((row,col))
    while queue:
        row,col=queue.popleft()
        for i in range(0,4):
            nRow=row+dRow[i]
            nCol=col+dCol[i]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>M-1):
                continue
            if(not visited[nRow][nCol] and maze[nRow][nCol]==1):
                visited[nRow][nCol]=True
                queue.append((nRow,nCol))
                distance[nRow][nCol]=distance[row][col]+1

N,M = map(int,input().split())
maze=[]
for _ in range(N):
    maze.append(list(map(int,input())))

visited=[[False for _ in range(M)] for i in range(N)]
distance=[[0 for _ in range(M)] for i in range(N)]
distance[0][0]=1

start=(0,0)

bfs(start)
print(distance)
print(distance[N-1][M-1])