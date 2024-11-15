from collections import deque

N = int(input())

results=[]

RGP_map = []
isVisited = [[False for _ in range(N)] for i in range(N)]

for _ in range(N):
    RGP_map.append(list(input()))

def bfs(start):
    queue = deque()
    dRow = [-1,1,0,0]
    dCol = [0,0,1,-1]
    queue.append(start)
    isVisited[start[0]][start[1]]=True
    
    while queue:
        ele = queue.popleft()
        color = ele[2]
        for i in range(len(dRow)):
            nRow = ele[0]+dRow[i]
            nCol = ele[1]+dCol[i]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>N-1):
                continue
            if(not isVisited[nRow][nCol] and RGP_map[nRow][nCol]==color):
                queue.append((nRow,nCol,color))
                isVisited[nRow][nCol]=True
    return

count=0
for row in range(N):
    for col in range(N):
        if(not isVisited[row][col]):
            color = RGP_map[row][col]
            bfs((row,col,color))
            count+=1
            
print(count, end=" ")

count=0
isVisited = [[False for _ in range(N)] for i in range(N)]

for row in range(N):
    for col in range(N):
        if(RGP_map[row][col]=="G"):
            RGP_map[row][col]="R"

        
for row in range(N):
    for col in range(N):
        if(not isVisited[row][col]):
            color = RGP_map[row][col]
            bfs((row,col,color))
            count+=1

print(count)

