import heapq

def dij(start,end):
    INF = 10e9
    distance = [INF for _ in range(N+1)]
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v,cost in graph[now]:
            if(distance[v]>dist+cost):
                distance[v]=cost+dist
                heapq.heappush(q,(dist+cost,v))
    return distance[end] 

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

res = dij(1,N)
print(res)
