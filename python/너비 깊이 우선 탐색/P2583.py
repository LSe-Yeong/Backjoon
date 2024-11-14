from collections import deque

resultCount=[]

def bfs(start):
    queue = deque()
    queue.append(start)
    count=1
    isVisited[row][col]=True
    dRow=[1,-1,0,0]
    dCol=[0,0,1,-1]
    while queue:
        ele = queue.popleft()
        for i in range(len(dRow)):
            nRow=ele[0]+dRow[i]
            nCol=ele[1]+dCol[i]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>M-1):
                continue
            if(not isVisited[nRow][nCol] and my_map[nRow][nCol]==0):
                queue.append((nRow,nCol))
                count+=1
                isVisited[nRow][nCol]=True  
    return count

N,M,K = map(int,input().split())

my_map=[[0 for _ in range(M)] for i in range(N)]
isVisited = [[False for _ in range(M)] for i in range(N)]

for k in range(K):
    col1,row1,col2,row2 = map(int,input().split())
    for r in range(row1,row2):
        for c in range(col1,col2):
            my_map[r][c]=1

for row in range(N):
    for col in range(M):
        if(not isVisited[row][col] and my_map[row][col]==0):
            resultCount.append(bfs((row,col)))

resultCount.sort()
print(len(resultCount))
for item in resultCount:
    print(item, end=" ")