from collections import deque

def bfs(start):
    distance = [0 for _ in range(N+1)]
    queue=deque()
    distance[start]=1
    queue.append(start)
    
    while queue:
        ele = queue.popleft()
        for v in graph[ele]:
            if(distance[v]==0):
                distance[v]=distance[ele]+1
                queue.append(v)
                if(distance[v]==K+1):
                    result.append(v)
    return distance
    
N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
result=[]

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)

distance = bfs(X)
result.sort()

if(len(result)==0):
    print(-1)
else:
    for v in result:
        print(v)
        