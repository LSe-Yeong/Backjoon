import heapq

def dij(start):
    queue=[]
    distance[start]=0
    heapq.heappush(queue,(0,start))
    while queue:
        dist, now = heapq.heappop(queue)
        if(distance[now]<dist):
            continue
        if(not now+1>=max_N):
            if(distance[now+1]>dist+1):
                distance[now+1]=dist+1
                heapq.heappush(queue,(dist+1,now+1))
        if(not now-1<0):
            if(distance[now-1]>dist+1):
                distance[now-1]=dist+1
                heapq.heappush(queue,(dist+1,now-1))
        if(not now*2>=max_N):
            if(distance[now*2]>dist):
                distance[now*2]=dist
                heapq.heappush(queue,(dist,now*2))
    

N,K = map(int,input().split())
INF = 10e9
max_N = 100001

distance = [INF for _ in range(max_N)]

dij(N)

print(distance[K])