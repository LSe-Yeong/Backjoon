from collections import deque

N, M = map(int,input().split())

graph=[[] for _ in range(N+1)]

for i in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[False for _ in range(N+1)]
count = 0

def bfs(start):
    queue=deque()
    visited[start]=True
    queue.append(start)
    
    while queue:
        ele = queue.popleft()
        for i in range(len(graph[ele])):
            if(not visited[graph[ele][i]]):
                queue.append(graph[ele][i])
                visited[graph[ele][i]]=True    

def dfs(start):
    visited[start]=True
    for i in graph[start]:
        if(not visited[i]):
            dfs(i)

for i in range(1,N+1):
    if(not visited[i]):
        count+=1
        dfs(i)
print(count)