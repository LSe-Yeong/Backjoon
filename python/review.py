# # 4 5 1
# # 1 2
# # 1 3
# # 1 4
# # 2 4
# # 3 4

# def dfs(start):
#     isVisited[start]=True
#     print(start,end=" ")
#     for v in graph[start]:
#         if not isVisited[v]:
#             dfs(v)

# from collections import deque

# def bfs(start):
#     q = deque()
#     q.append(start)
#     print(start,end=" ")
#     isVisited[start]=True
#     while q:
#         ele = q.popleft()
#         for v in graph[ele]:
#             if not isVisited[v]:
#                 print(v,end=" ")
#                 q.append(v)
#                 isVisited[v]=True

# n,v,start = map(int,input().split())
# graph = [[] for i in range(n+1)]
# for i in range(v):
#     u,v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# isVisited = [False for i in range(n+1)]
# dfs(start)
# print()

# isVisited = [False for i in range(n+1)]
# bfs(start)

#이진 탐색
# arr=[0,1,4,6,8,9,12,16,19,22]
# M = int(input())

# left = 0
# right = len(arr)-1
# idx = -1

# while left<=right:
#     mid = (left+right)//2
#     if arr[mid]==M:
#         idx=mid
#         break
#     elif arr[mid] < M:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(f'idx => {idx}')

#DP

#다익스트라
# import heapq
# def dij(start):
#     q=[]
#     heapq.heappush(q,(0,start))
#     distance[start] = 0
#     while q:
#         dist,now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for v,w in graph[now]:
#             cost = dist + w
#             if cost < distance[v]:
#                 distance[v] = cost
#                 heapq.heappush(q,(cost,v))
#     return

# import sys
# INF = 10e10
# V,E = map(int,input().split())
# start = int(input())
# graph = [[] for i in range(V+1)]
# for i in range(E):
#     u,v,w = map(int,input().split())
#     graph[u].append((v,w))

# distance = [INF for i in range(V+1)]

# dij(start)
# print(distance)
# for i in range(1,len(distance)):
#     if distance[i]==INF:
#         print("INF")
#     else:
#         print(distance[i])


st = "aaabbbaaccc"
st_list = []

idx = 0
while idx < len(st)-1:
    count = 1
    while idx != len(st) - 1 and st[idx] == st[idx+1]:
        count += 1
        idx += 1
    st_list.append((st[idx],count))
    idx += 1

result = 0
for i in range(len(st_list)-1):
    ch, num = st_list[i]
    value = st_list[i+1][1]
    result += min(num,value)

    if num < value:
        print(ch,result)
        continue

    idx = i + 2
    subCount = 0
    while idx != len(st_list) and st_list[idx][1] == value:
        idx += 1
        subCount += 1
    
    if idx == len(st_list):
        result += subCount
        print(ch,result)
        continue

    if st_list[idx][1] > value:
        result += subCount
        result += 1
    print(ch,result)

print(result)
