import heapq

N,M,C = map(int,input().split())
INF = 100000000
city = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for _ in range(M):
    u,v,w = map(int,input().split())
    city[u].append((v,w))
    
def dij(start):
    queue = []
    distance[start]=0
    heapq.heappush(queue,(0,start))
    while queue:
        dist, now = heapq.heappop(queue)
        if(distance[now]<dist):
            continue
        for v in city[now]:
            cost = dist + v[1]
            if(cost<distance[v[0]]):
                distance[v[0]] = cost
                heapq.heappush(queue,(cost,v[0]))

dij(C)

count=0
max_v=0
for d in distance:
    if d!=0 and d!=INF:
       count+=1
       max_v=max(max_v,d)

print(count,max_v) 
        
