import sys
import heapq

V,E = map(int,sys.stdin.readline().strip().split()) # 정점, 간선
K = int(sys.stdin.readline().strip()) # 시작점

INF = int(1e9) # 초기값
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().strip().split())
    graph[u].append((v,w)) # (정점, 가중치)
        
def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    distance[start]=0
    
    while queue:
        dist,now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for v,w in graph[now]:
            if dist+w < distance[v]:
                distance[v] = dist+w
                heapq.heappush(queue,(dist+w,v))

dijkstra(K)

for n in range(1,V+1):
    if distance[n] == INF:
        distance[n] = "INF"
        
for i in range(1,V+1):
    print(distance[i])