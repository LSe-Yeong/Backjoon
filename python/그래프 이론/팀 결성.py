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
        
N,M = map(int,input().split())
parents = [0 for _ in range(N+1)]

for i in range(N+1):
    parents[i]=i

for _ in range(M):
    t,u,v = map(int,input().split())
    if t==0:
        union(parents,u,v)
    else:
        #같은팀 여부 (부모가 같은지)
        if(find_parent(parents,u)==find_parent(parents,v)):
            print("YES")
        else:
            print("NO")
            
print(parents)
            