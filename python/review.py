# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

def dfs(start):
    isVisited[start]=True
    print(start,end=" ")
    for v in graph[start]:
        if not isVisited[v]:
            dfs(v)

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    print(start,end=" ")
    isVisited[start]=True
    while q:
        ele = q.popleft()
        for v in graph[ele]:
            if not isVisited[v]:
                print(v,end=" ")
                q.append(v)
                isVisited[v]=True

n,v,start = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(v):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

isVisited = [False for i in range(n+1)]
dfs(start)
print()

isVisited = [False for i in range(n+1)]
bfs(start)

