from collections import deque

def print_array(arr):
    for ar in arr:
        for v in ar:
            print(v, end=" ")
        print()
    return
    
def bfs(start):
    dRow=[1,0,-1,0]
    dCol=[0,1,0,-1]
    q = deque()
    q.append(start)
    distance[start[0]][start[1]]=0
    
    while q:
        r,c = q.popleft()
        for i in range(len(dRow)):
            nRow = r + dRow[i]
            nCol = c + dCol[i]
            if(nRow < 0 or nRow>row-1 or nCol<0 or nCol>col-1):
                continue
            if(distance[nRow][nCol]==-1 and my_map[nRow][nCol]==1):
                q.append((nRow,nCol))
                distance[nRow][nCol] = distance[r][c] + 1
    return

import sys

row, col = map(int,sys.stdin.readline().split())
my_map = []
distance = [[-1 for _ in range(col)] for i in range(row)]

for _ in range(row):
    my_map.append(list(map(int,sys.stdin.readline().split())))

start = []

for r in range(row):
    for c in range(col):
        if(my_map[r][c]==0):
            distance[r][c]=0
        elif(my_map[r][c]==2):
            start.append((r,c))  

bfs(start[0])

print_array(distance)
            
