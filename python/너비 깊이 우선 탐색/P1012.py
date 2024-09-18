from collections import deque
t=int(input())

def bfs(start):
    queue=deque()
    dRow=[0,1,-1,0]
    dCol=[1,0,0,-1]
    row=start[0]
    col=start[1]
    visited[row][col]=True
    queue.append(start)
    while queue:
        ele = queue.popleft()
        cRow=ele[0]
        cCol=ele[1]
        for i in range(4):
            nRow=cRow+dRow[i]
            nCol=cCol+dCol[i]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>M-1):
                continue
            if(not visited[nRow][nCol] and baechu[nRow][nCol]==1):
                visited[nRow][nCol]=True
                queue.append([nRow,nCol])


for _ in range(0,t):
    M,N,K=map(int,input().split())
    baechu=[[0 for i in range(M)] for j in range(N)]
    visited=[[False for i in range(M)] for j in range(N)]
    count=0

    for i in range(K):
        col,row=map(int,input().split())
        baechu[row][col]=1
    for row in range(N):
        for col in range(M):
            if(not visited[row][col] and baechu[row][col]==1):
               count+=1
               bfs([row,col])
    print(count)


    
