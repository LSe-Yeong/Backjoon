from collections import deque
T = int(input())

def bfs(start,V):
    queue=deque()
    queue.append(start)
    isVisited = [False for _ in range(V+1)]
    isVisited[start]=True
    status[start]=1
    while queue:
        ele = queue.popleft()
        for v in graph[ele]:
            if(status[v]==0):
                queue.append(v)
                if(status[ele]==1):
                    status[v]=2
                elif(status[ele]==2):
                    status[v]=1
            elif(status[v]==status[ele]):
                return "NO"
    return "YES"
    
for _ in range(T):
    flag=True
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    status = [0 for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1,V+1):
        if(status[i]==0):
            if(bfs(i,V)=="NO"):
                flag=False
                print("NO")
                break
    if(flag):
        print("YES")