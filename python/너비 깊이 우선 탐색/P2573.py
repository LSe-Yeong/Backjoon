from collections import deque

def melting(m):
    melt_list = []
    for r in range(N):
        for c in range(M):
            if m[r][c] == 0:
                continue
            
            count = 0
            if m[r+1][c] == 0:
                count += 1
            if m[r-1][c] == 0:
                count += 1
            if m[r][c+1] == 0:
                count += 1
            if m[r][c-1] == 0:
                count += 1
            melt_list.append((r,c,count))
    
    for r,c,count in melt_list:
        m[r][c] -= count
        if m[r][c] < 0:
            m[r][c] = 0

def no_binha(m):
    flag = True
    for r in range(N):
        for c in range(M):
            if m[r][c] != 0:
                flag = False
    return flag

def bfs(start,isVisit):
    dRow = [-1,1,0,0]
    dCol = [0,0,1,-1]
    q = deque()
    isVisit[start[0]][start[1]] = True
    q.append(start)

    while q:
        row, col = q.popleft()
        for i in range(4):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if nRow > N-1 or nRow < 0 or nCol > M-1 or nCol < 0:
                continue
            if ice_map[nRow][nCol] != 0 and not isVisit[nRow][nCol]:
                isVisit[nRow][nCol] = True
                q.append((nRow,nCol))
        
N,M = map(int,input().split())
ice_map = []
for _ in range(N):
    ice_map.append(list(map(int,input().split())))

result = 1

while True:
    if no_binha(ice_map):
        result = 0
        break 

    melting(ice_map)

    isVisit = [[False for i in range(M)] for j in range(N)]
    count = 0
    for r in range(N):
        for c in range(M):
            if not isVisit[r][c] and ice_map[r][c] != 0:
                count += 1
                bfs((r,c),isVisit)
    
    if count >= 2:
        break

    result += 1

print(result)
