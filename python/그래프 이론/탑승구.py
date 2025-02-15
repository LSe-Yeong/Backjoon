def find_p(p,x):
    if p[x]!=x:
        p[x] = find_p(p,p[x])
    return p[x]

def union(p,a,b):
    a = find_p(p,a)
    b = find_p(p,b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

N = int(input())
M = int(input())
parent = [0 for _ in range(N+1)]

for i in range(N+1):
    parent[i]=i
  
result=0  
for i in range(M):
    v = int(input())
    node = find_p(parent,v)
    if node == 0:
        break
    else:
        union(parent,node,node-1)
        result+=1

print(result)

    