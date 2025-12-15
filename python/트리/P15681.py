import sys

def makeTree(cur,par):
    if par == -1:
        parent[cur] = -1
    for v in graph[cur]:
        if v != par:
            child[cur].append(v)
            parent[v] = cur
            makeTree(v,cur)

def countSubTree(cur):
    size[cur] = 1
    for v in child[cur]:
        countSubTree(v)
        size[cur] += size[v]

sys.setrecursionlimit(10**5)
N,R,Q = map(int,input().split())

graph = [[] for i in range(N+1)]
child = [[] for i in range(N+1)]
parent = [0 for i in range(N+1)]
size = [0 for i in range(N+1)]

for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

makeTree(R,-1)
countSubTree(R)

for i in range(Q):
    print(size[int(input())])

