import heapq

V,E = map(int,input().split())
K=int(input())
INF = 10e9

graph = [[] for _ in range(V+1)]
distance = [INF for _ in range(V+1)]

def dij(start):
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
                

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

dij(K)

for i in range(1,len(distance)):
    if(distance[i]==INF):
        print("INF")
    else:
        print(distance[i])
