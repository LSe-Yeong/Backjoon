import heapq

N = int(input())
q=[]

for _ in range(N):
    v = int(input())
    heapq.heappush(q,v)

sum=0
while len(q)!=1:
    v1 = heapq.heappop(q)
    v2 = heapq.heappop(q)
    sum+=(v1+v2)
    heapq.heappush(q,v1+v2)

print(sum)