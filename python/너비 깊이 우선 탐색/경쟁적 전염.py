from collections import deque

N,K = map(int,input().split())
my_map = []
time=[[0 for _ in range(N)] for i in range(N)]

for _ in range(K):
    my_map.append(list(map(int,input().split())))

S,X,Y = map(int,input().split())

def bfs(start):
    dRow=[0,1,-1,0]
    dCol=[1,0,0,-1]
    q=deque()
    q.append(start)
    while q:
        ele = q.popleft()
        for i in range(len(dRow)):
            nRow = dRow[i] + ele[0]
            nCol = dCol[i] + ele[1]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>N-1):
                continue
            if(time[nRow][nCol]==0 or time[ele[0]][ele[1]]+1 <= time[nRow][nCol]):
                if(time[ele[0]][ele[1]]+1 == time[nRow][nCol]):
                    my_map[nRow][nCol] = min(my_map[ele[0]][ele[1]],my_map[nRow][nCol]) 
                else:
                    my_map[nRow][nCol] = my_map[ele[0]][ele[1]]
                time[nRow][nCol] = time[ele[0]][ele[1]] +1
                q.append((nRow,nCol))
    return

bfs_dot = []
for r in range(N):
    for c in range(N):
        if(my_map[r][c]!=0):
            time[r][c]=1
            bfs_dot.append((r,c))

for v in bfs_dot:
    bfs(v)

for r in range(N):
    for c in range(N):
        if(time[r][c]>S+1):
            my_map[r][c]=0

print(my_map[X-1][Y-1])
    
            
