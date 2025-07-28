from collections import deque

def topology_sort():
    result = []
    q = deque()
    for i in range(1,N+1):
        if indegrees[i]==0:
            q.append((i,1))
    
    while q:
        now,level = q.popleft()
        result.append((now,level))
        for v in graph[now]:
            indegrees[v]-=1
            if indegrees[v]==0:
                q.append((v,level+1))
    return result

            

N,M = map(int,input().split())
indegrees = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    indegrees[b]+=1
    graph[a].append(b)

result = topology_sort()
result.sort(key=lambda x:x[0])

for v,l in result:
    print(l,end=" ")
