import heapq

N, M = map(int,input().split())
card = list(map(int,input().split()))
queue=[]

for i in range(N):
    heapq.heappush(queue,card[i])

for m in range(M):
    ele1 = heapq.heappop(queue)
    ele2 = heapq.heappop(queue)
    heapq.heappush(queue,ele1+ele2)
    heapq.heappush(queue,ele1+ele2)
    
sum=0

for i in range(N):
    sum+=heapq.heappop(queue)

print(sum)