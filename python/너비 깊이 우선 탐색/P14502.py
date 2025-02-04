import copy
from collections import deque
from itertools import combinations

def bfs(start,test_map):
    dRow=[0,1,-1,0]
    dCol=[1,0,0,-1]
    queue = deque()
    queue.append(start)
    test_map[start[0]][start[1]]=3
    while queue:
        ele = queue.popleft()
        for i in range(len(dRow)):
            nRow = ele[0] + dRow[i]
            nCol = ele[1] + dCol[i]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>M-1):
                continue
            if(test_map[nRow][nCol]==0):
                test_map[nRow][nCol]=3
                queue.append([nRow,nCol])
    return

N,M = map(int,(input().split()))
my_map=[]
wall=[]

for _ in range(N):
    my_map.append(list(map(int,input().split())))

for r in range(N):
    for c in range(M):
        if(my_map[r][c]==0):
            wall.append([r,c])

wall_list = list(combinations(wall,3))

max_count=-1
for walls in wall_list:
    test_map = copy.deepcopy(my_map)
    for wall in walls:
        test_map[wall[0]][wall[1]]=1
    for r in range(N):
        for c in range(M):
            if(test_map[r][c]==2):
                bfs([r,c],test_map)
    count=0
    for r in range(N):
        for c in range(M):
            if(test_map[r][c]==0):
                count+=1
    if(max_count<=count):
        max_count=count

print(max_count)
        
