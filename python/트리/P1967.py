from collections import deque

def bfs(start):
    distance = [-1 for i in range(N+1)]
    q = deque()
    q.append((start,0))
    distance[start] = 0
    while q:
        now,cost = q.popleft()
        for v,w in graph[now]:
            if distance[v] == -1:
                distance[v] = cost + w
                q.append((v,distance[v]))  
    return max(distance)

N = int(input())

graph = [[] for i in range(N+1)]

result = -10e9
for _ in range(N-1):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

for i in range(1,N+1):
    result = max(result,bfs(i))

print(result)
