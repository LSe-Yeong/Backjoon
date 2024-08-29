from collections import deque

def dfs(start):
    visited[start['row']][start['col']]=True
    for i in range(0,4):
        nRow=start['row']+dRow[i]
        nCol=start['col']+dCol[i]
        if(nRow<0 or nRow>=N or nCol<0 or nCol >= M):
                continue
        if(not visited[nRow][nCol] and ice_map[nRow][nCol]==0):
                dfs({'row':nRow,'col':nCol})
                
def bfs(start):
    visited[start['row']][start['col']]=True
    queue.append(start)

    while queue:
        element=queue.popleft()
        for i in range(0,4):
            nRow=element['row']+dRow[i]
            nCol=element['col']+dCol[i]
            if(nRow<0 or nRow>=N or nCol<0 or nCol >= M):
                continue
            if(not visited[nRow][nCol] and ice_map[nRow][nCol]==0):
                visited[nRow][nCol]=True
                queue.append({'row':nRow,'col':nCol})
                
N,M = map(int,input().split())
ice_map=[]
visited=[[False for col in range(M)] for _ in range(N)]
count=0

for _ in range(0,N):
    ice_map.append(list(map(int,input())))

dRow=[0,-1,0,1]
dCol=[1,0,-1,0]
queue=deque()
                
for i in range(N):
    for j in range(M):
        if(ice_map[i][j]==0  and not visited[i][j]):
            dfs({'row':i,'col':j})
            count=count+1
            
print(count)




