from collections import deque

def search_area(start):
    dRow = [-1,1,0,0]
    dCol = [0,0,1,-1]
    q = deque()
    q.append(start)
    arr[start[0]][start[1]] = 2

    while q:
        row,col = q.popleft()
        for i in range(len(dRow)):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if nRow < 0 or nRow > N-1 or nCol < 0 or nCol > M-1:
                continue
            if arr[nRow][nCol] not in [1,2]:
                q.append((nRow,nCol))
                arr[nRow][nCol] = 2

def remove_cheese():
    remove_buffer = []
    dRow = [1,-1,0,0]
    dCol = [0,0,1,-1]
    for r in range(N):
        for c in range(M):
            count = 0
            for i in range(len(dRow)):
                nRow = r + dRow[i]
                nCol = c + dCol[i]
                if nRow > N-1 or nRow < 0 or nCol > M-1 or nCol < 0:
                    continue
                if arr[nRow][nCol] == 2:
                    count += 1
            if count >= 2:
                remove_buffer.append((r,c))
    for row,col in remove_buffer:
        arr[row][col] = 0

def isEnd():
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                return False
    return True

N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

result = 0
while True:
    result += 1
    search_area((0,0))
    remove_cheese()
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 2:
                arr[r][c] = 0
    if(isEnd()):
        break

print(result)