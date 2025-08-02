# 7
# 3
# 1
# 1
# 5
# 5
# 4
# 6

def dfs(now,start,visited):
    visited[now] = True
    for v in graph[now]:
        if not visited[v]:
            dfs(v,start,visited)
        elif visited[v] and v==start:
            result.append(v)

N = int(input())
result = []

graph = [[] for i in range(N+1)]
for i in range(N):
    graph[int(input())].append(i+1)

for i in range(1,N+1):
    visited = [False for i in range(N+1)]
    dfs(i,i,visited)
print(result)



