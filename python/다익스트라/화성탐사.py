import heapq

N = int(input())
INF = 10e15

spot = []
distance = [[INF for _ in range(N)] for i in range(N)]

for _ in range(N):
    spot.append(list(map(int,input().split())))

def dij(start):
    dRow = [-1,0,1,0]
    dCol = [0,-1,0,1]
    w,r,c = start
    distance[r][c] = w
    q = []
    heapq.heappush(q,(w,r,c))
    while q:
        w,r,c = heapq.heappop(q)
        if(distance[r][c] < w):
            continue
        for i in range(len(dRow)):
            nRow = r + dRow[i]
            nCol = c + dCol[i]
            if(nRow<0 or nRow>N-1 or nCol<0 or nCol>N-1):
                continue
            if(distance[nRow][nCol]>w+spot[nRow][nCol]):
                distance[nRow][nCol] = w + spot[nRow][nCol]
                heapq.heappush(q,(distance[nRow][nCol],nRow,nCol))
        
dij((spot[0][0],0,0))

print(distance)