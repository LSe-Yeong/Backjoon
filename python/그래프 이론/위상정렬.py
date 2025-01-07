from collections import deque

V, E = map(int,input().split())
indegrees = [0 for _ in range(V+1)]
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    indegrees[v]+=1

def topology_sort():
    result=[]
    queue = deque()
    
    for i in range(1,V+1):
        if(indegrees[i]==0):
            queue.append(i)
    
    while queue:
        now = queue.popleft()
        result.append(now)
        
        for v in graph[now]:
            indegrees[v]-=1
            if(indegrees[v]==0):
                queue.append(v)
    return result

print(topology_sort())
    