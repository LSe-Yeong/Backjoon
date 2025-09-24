# from collections import deque

# def bfs(start):
#     distance = [0 for _ in range(N+1)]
#     queue=deque()
#     distance[start]=1
#     queue.append(start)
    
#     while queue:
#         ele = queue.popleft()
#         for v in graph[ele]:
#             if(distance[v]==0):
#                 distance[v]=distance[ele]+1
#                 queue.append(v)
#                 if(distance[v]==K+1):
#                     result.append(v)
#     return distance
    
# N,M,K,X = map(int,input().split())
# graph = [[] for _ in range(N+1)]
# result=[]

# for _ in range(M):
#     u,v = map(int,input().split())
#     graph[u].append(v)

# distance = bfs(X)
# result.sort()

# if(len(result)==0):
#     print(-1)
# else:
#     for v in result:
#         print(v)
from collections import deque
def bfs(start):  
    distance = [0 for _ in range(N+1)]
    q = deque()
    q.append(start)
    distance[start] = 1
    while q:
        dot = q.popleft()
        for v in graph[dot]:
            if distance[v] == 0:
                q.append(v)
                distance[v] = distance[dot] + 1
    return distance

N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)

dist_list = bfs(X)

if not K+1 in dist_list:
    print(-1)
else:
    for i in range(1,len(dist_list)):
        if K+1 == dist_list[i]:
            print(i)

