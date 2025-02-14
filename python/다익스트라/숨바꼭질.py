from collections import deque
import heapq

N, M = map(int,(input().split()))

## BFS 를 이용한 풀이
# graph=[[] for _ in range(N+1)]
# distance = [-1 for _ in range(N+1)]

# for _ in range(M):
#     u,v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# def bfs(start):
#     q = deque()
#     q.append(start)
#     distance[start]=0
    
#     while q:
#         now = q.popleft()
#         for v in graph[now]:
#             if(distance[v]==-1):
#                 distance[v] = distance[now]+1
#                 q.append(v)

# bfs(1)    
# print(distance.index(max(distance)),end=" ")
# print(max(distance), end=" ")
# print(distance.count(max(distance)))

INF = 10e10
graph=[[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append((v,1))
    graph[v].append((u,1))

def dij(start):
    q = []
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if(distance[now]<dist):
            continue
        for v,w in graph[now]:
            if(distance[v] > dist+w):
                distance[v]=dist+w
                heapq.heappush(q,(dist+w,v))

dij(1)
print(distance) 
    