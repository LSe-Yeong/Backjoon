import heapq

N,E = map(int,input().split())

city = [[] for _ in range(N+1)]
INF = 1000000000

for _ in range(E):
    u,v = map(int,input().split())
    city[u].append((v,1))
    city[v].append((u,1))

X,K = map(int,input().split())

def dij(start):
    distance = [INF for _ in range(N+1)]
    queue = []
    distance[start]=0
    heapq.heappush(queue,(0,start))
    while queue:
        dist, now = heapq.heappop(queue)
        
        if(distance[now]<dist):
            continue
        for v in city[now]:
            nV = v[0]
            nW = v[1]
            cost = dist +nW
            if(cost<distance[nV]):
                distance[nV] = cost
                heapq.heappush(queue,(cost,nV))
    return distance


def fw():
    
    return

firstDistance = dij(1)
secondDistance = dij(K)
result =firstDistance[K]+secondDistance[X]
if(result>=INF):
    print(-1)
else:
    print(result)
    




