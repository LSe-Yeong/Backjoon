# from collections import deque

# N,L,R = map(int,input().split())
# country = []
# for _ in range(N):
#     country.append(list(map(int,input().split())))

# def bfs(start):
#     dRow = [-1,0,1,0]
#     dCol = [0,1,0,-1]
#     uni = []
#     q = deque()
#     q.append(start)
#     Visited[start[0]][start[1]]=1
#     uni.append((start[0],start[1]))
    
#     while q:
#         ele = q.popleft()
#         for i in range(len(dRow)):
#             nRow = ele[0] + dRow[i]
#             nCol = ele[1] + dCol[i]
#             if(nRow<0 or nRow>N-1 or nCol<0 or nCol>N-1):
#                 continue
#             diff = abs(country[nRow][nCol] - ele[2])
#             if(diff>=L and diff<=R and Visited[nRow][nCol]==0):
#                 q.append((nRow,nCol,country[nRow][nCol]))
#                 uni.append((nRow,nCol))
#                 Visited[nRow][nCol]=1
#     unions.append(uni)
#     return 

# count=0
# while True:
#     unions=[]
#     Visited = [[0 for _ in range(N)] for i in range(N)]
#     for r in range(N):
#         for c in range(N):
#             if(Visited[r][c]==0):
#                 bfs((r,c,country[r][c]))
    
#     if(len(unions)==N*N):
#         print(count)
#         break

#     for union in unions:
#         sum=0
#         for pot in union:
#             r,c = pot
#             sum+=country[r][c]
#         for pot in union:
#             r,c = pot
#             country[r][c] = int(sum/len(union))
#     count+=1
from collections import deque

def bfs(start,isVisited,g):
    dRow = [-1,0,1,0]
    dCol = [0,1,0,-1]
    value = city[start[0]][start[1]]
    q = deque()
    q.append(start)
    g.append(start)
    isVisited[start[0]][start[1]] = True

    while q:
        row, col = q.popleft()
        for i in range(len(dRow)):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if nRow > N-1 or nRow < 0 or nCol > N-1 or nCol < 0:
                continue
            if not isVisited[nRow][nCol] and L<=abs(city[row][col]-city[nRow][nCol])<=R:
                q.append((nRow,nCol))
                g.append((nRow,nCol))
                isVisited[nRow][nCol] = True
                value += city[nRow][nCol]
    return value

N,L,R = map(int,input().split())
city = []
for _ in range(N):
    city.append(list(map(int,input().split())))

day = 1
isOver = False
while not isOver:
    groups = []
    values = []
    union = set()
    isVisited = [[False for _ in range(N)] for i in range(N)]
    for r in range(N):
        for c in range(N):
            group = []
            if not isVisited[r][c]:
                value = bfs((r,c),isVisited,group)
                values.append(value)
                groups.append(group)
    
    for i in range(len(groups)):
        change_value = values[i] // len(groups[i])
        for r,c in groups[i]:
            city[r][c] = change_value
    if len(groups) == N*N:
        isOver=True
    day+=1

print(day-2)