import sys
import heapq

N,E =map(int,input().split())
graph = [[] for _ in range(N+1)]
INF=sys.maxsize

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

v1,v2 = map(int,input().split())

def dijkstar(start):
    dist=[INF for _ in range(N+1)]
    queue=[]
    dist[start]=0
    heapq.heappush(queue,(0,start))
    
    while queue:
        distance,now = heapq.heappop(queue)
        if(dist[now]<distance):
            continue
        for v,w in graph[now]:
            cost = distance + w
            if(dist[v] > cost):
                dist[v]=cost
                heapq.heappush(queue,(cost,v))
    return dist

start=dijkstar(1)
mid=dijkstar(v1)
mid2=dijkstar(v2)
               
print(min(start[v1]+mid[v2]+mid2[N],start[v2]+mid2[v1]+mid[N]))
