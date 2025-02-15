def find_p(p,x):
    if(p[x]!=x):
        p[x] = find_p(p,p[x])
    return p[x]

def union(p,a,b,):
    a = find_p(p,a)
    b = find_p(p,b)
    if a<b:
        p[b]=a
    else:
        p[a]=b
        
def crus(p,edges):
    result=0
    for cost,u,v in edges:
        if(find_p(p,u)!=find_p(p,v)):
            result+=cost
            union(p,u,v)
    return result

N = int(input())
x = []
y = []
z = []
e = []

parents = [0 for _ in range(N)]
for i in range(1,N):
    parents[i] = i

for i in range(N):
    a,b,c = map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

for i in range(N-1):
    e.append((abs(x[i+1][0]-x[i][0]),x[i+1][1],x[i][1]))
    e.append((abs(y[i+1][0]-y[i][0]),y[i+1][1],y[i][1]))
    e.append((abs(z[i+1][0]-z[i][0]),z[i+1][1],z[i][1]))

e.sort()

print(crus(parents,e))