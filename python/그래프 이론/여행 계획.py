def find_p(parent,x):
    if parent[x] != x:
        parent[x] = find_p(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_p(parent,a)
    b = find_p(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int,input().split())
city = []

parents = [0 for i in range(N)]
for i in range(N):
    parents[i]=i

for _ in range(N):
    city.append(list(map(int,input().split())))
course = list(map(int,input().split()))

for r in range(N):
    for c in range(r,N):
        if(city[r][c]==1):
            union(parents,r,c)

isResult = True
for i in range(len(course)-1):
    if(find_p(parents,course[i])!=find_p(parents,course[i+1])):
        isResult = False
        break

if(isResult):
    print("YES")
else:
    print("NO")

