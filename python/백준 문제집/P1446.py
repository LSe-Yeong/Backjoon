# def isShortCut(idx):
#     shortcut=[10e9,10e9,10e9]
#     for i in range(len(shortcuts)):
#         if(shortcuts[i][1]==idx):
#             if(shortcut[2]>shortcuts[i][2]):
#                 shortcut=shortcuts[i]
#     return shortcut

# import sys

# N, D = map(int,sys.stdin.readline().split())
# shortcuts = []
# DP = [0 for _ in range(D+1)]

# for _ in range(N):
#     shortcuts.append(list(map(int,sys.stdin.readline().split())))

# for i in range(1,D+1):
#     shortcut = isShortCut(i)
#     if(shortcut[2]!=10e9):
#         DP[i]=min(DP[i-1]+1,DP[shortcut[0]]+shortcut[2])
#     else:
#         DP[i]=DP[i-1]+1

# print(DP[-1])        

import heapq

def dij(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v,w in graph[now]:
            if(distance[v]>dist+w):
                distance[v]=dist+w
                heapq.heappush(q,(dist+w,v))
    return
    
import sys

N, D = map(int,sys.stdin.readline().split())
shortcuts = []
graph=[[] for i in range(D+1)]
distance = [10e9 for i in range(D+1)]

for i in range(D):
    graph[i].append((i+1,1))
    
for _ in range(N):
    u,v,w = map(int,sys.stdin.readline().split())
    if(v<D+1):
        graph[u].append((v,w))

dij(0)
print(distance[-1])