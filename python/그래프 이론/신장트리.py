def find_parent(parent,x):
    if(parent[x]!=x):
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
    
edges=[]    
result=0

n, e =map(int,input().split())
parents = [0 for _ in range(n+1)]
print(parents)

for _ in range(e):
    u,v,cost = map(int,input().split())
    edges.append((cost,u,v))

for i in range(1,n+1):
    parents[i]=i
    

#알고리즘
edges.sort()

for edge in edges:
    cost,u1,v1 = edge
    print(edge)
    if find_parent(parents,u1) != find_parent(parents,v1):
        union(parents,u1,v1)
        result+=cost

print(result)