from collections import deque

N,L,R = map(int,input().split())
country = []
for _ in range(N):
    country.append(list(map(int,input().split())))

def bfs(start):
    dRow = [-1,0,1,0]
    dCol = [0,1,0,-1]
    uni = []
    q = deque()
    q.append(start)
    Visited[start[0]][start[1]]=1
    uni.append((start[0],start[1]))
    
    while q:
        ele = q.popleft()
        for i in range(len(dRow)):
            nRow = ele[0] + dRow[i]
            nCol = ele[1] + dCol[i]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>N-1):
                continue
            diff = abs(country[nRow][nCol] - ele[2])
            if(diff>=L and diff<=R and Visited[nRow][nCol]==0):
                q.append((nRow,nCol,country[nRow][nCol]))
                uni.append((nRow,nCol))
                Visited[nRow][nCol]=1
    unions.append(uni)
    return 

count=0
while True:
    unions=[]
    Visited = [[0 for _ in range(N)] for i in range(N)]
    for r in range(N):
        for c in range(N):
            if(Visited[r][c]==0):
                bfs((r,c,country[r][c]))
    
    if(len(unions)==N*N):
        print(count)
        break

    for union in unions:
        sum=0
        for pot in union:
            r,c = pot
            sum+=country[r][c]
        for pot in union:
            r,c = pot
            country[r][c] = int(sum/len(union))
    count+=1

