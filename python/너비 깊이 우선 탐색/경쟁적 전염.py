# from collections import deque

# N,K = map(int,input().split())
# my_map = []

# for _ in range(N):
#     my_map.append(list(map(int,input().split())))

# S,X,Y = map(int,input().split())

# def bfs(start):
#     dRow=[0,1,-1,0]
#     dCol=[1,0,0,-1]
#     q=deque(start)
#     while q:
#         value, s,row,col = q.popleft()
#         if(s==S):
#             break
#         for i in range(len(dRow)):
#             nRow = dRow[i] + row
#             nCol = dCol[i] + col
#             if(nRow<0 or nRow>N-1 or nCol<0 or nCol>N-1):
#                 continue
#             if(my_map[nRow][nCol]==0):
#                 my_map[nRow][nCol] = my_map[row][col]
#                 q.append([value,s+1,nRow,nCol])
#     return

# bfs_dot = []
# for r in range(N):
#     for c in range(N):
#         if(my_map[r][c]!=0):
#             bfs_dot.append((my_map[r][c],0,r,c))

# bfs_dot.sort()

# bfs(bfs_dot)

# print(my_map[X-1][Y-1])

from collections import deque 

def bfs(start):
    dRow = [1,-1,0,0]
    dCol = [0,0,1,-1]
    q = deque(start)
    while q:
        row,col,s,value = q.popleft()
        if s==S:
            break
        for i in range(len(dRow)):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if nRow < 0 or nRow > N-1 or nCol < 0 or nCol > N-1:
                continue
            if my_map[nRow][nCol] == 0:
                q.append((nRow,nCol,s+1,value))
                my_map[nRow][nCol] = my_map[row][col]
            

N,K =map(int,input().split())
my_map = []
for _ in range(N):
    my_map.append(list(map(int,input().split())))
S,X,Y = map(int,input().split())

virus_s = []

for r in range(N):
    for c in range(N):
        if my_map[r][c] != 0:
            virus_s.append((r,c,0,my_map[r][c]))

virus_s.sort(key=lambda x:x[3])

bfs(virus_s)

print(my_map[X-1][Y-1])