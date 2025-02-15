def find_p(p,x):
    if p[x]!=x:
        p[x]=find_p(p,p[x])
    return p[x]

def union(p,a,b):
    a = find_p(p,a)
    b = find_p(p,b)
    if a<b:
        p[b]=a
    else:
        p[a]=b
        
def crus(parent, edges):
    result = 0
    for edge in edges:
        cost,u,v = edge
        if find_p(parent,u) != find_p(parent,v):
            result+=cost
            union(parent,u,v)
    return result

N,M = map(int,input().split())

edges = []
parents = [0 for _ in range(N)]
for i in range(N):
    parents[i] = i

origin_sum=0
for _ in range(M):
    u,v,cost = map(int,input().split())
    origin_sum+=cost
    edges.append((cost,u,v))

edges.sort()
print(origin_sum - crus(parents,edges))
    