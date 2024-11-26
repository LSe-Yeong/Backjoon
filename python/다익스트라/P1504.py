import heapq

N,E = map(int,input().split())

def dij(start,end):
    distance = [INF for _ in range(N+1)]
    queue=[]   
    distance[start]=0
    heapq.heappush(queue,(0,start))
    while queue:
        dist, now = heapq.heappop(queue)
        if(distance[now]<dist):
            continue
        for v,w in graph[now]:
            if(distance[v]>dist+w):
                distance[v]=dist+w
                heapq.heappush(queue,(dist+w,v)) 
    return distance[end]

INF = 10e9
graph = [[] for _ in range(N+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

v1,v2 = map(int,input().split())

result = min(dij(1,v1)+dij(v1,v2)+dij(v2,N),dij(1,v2)+dij(v2,v1)+dij(v1,N))

if(result>=INF):
    print(-1)
else:
    print(result)
    