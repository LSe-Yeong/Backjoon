def find_parent(parent,x):
    if(parent[x]!=x):
        return find_parent(parent,parent[x])
    return parent[x]

#개선된 부모 찾기
def find_parent2(parent,x):
    if(parent[x]!=x):
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
#초기 부모는 자기 자신

#입력을 받다가 같은 부모가 나온다면 사이클임, 아니면 부모 합치기(같은 집합으로)
def isCycle(parent):
    a=1
    b=2
    if find_parent(parent,a) == find_parent(parent,b):
        return True
    else:
        union_parent(parent,a,b)
        
