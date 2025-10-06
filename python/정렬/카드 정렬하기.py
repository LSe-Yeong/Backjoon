# import heapq

# N = int(input())
# q=[]

# for _ in range(N):
#     v = int(input())
#     heapq.heappush(q,v)

# sum=0
# while len(q)!=1:
#     v1 = heapq.heappop(q)
#     v2 = heapq.heappop(q)
#     sum+=(v1+v2)
#     heapq.heappush(q,v1+v2)

# print(sum)


import heapq

N = int(input())
q = []
result = 0
for _ in range(N):
    heapq.heappush(q,int(input()))

while len(q) > 1:
    ele1 = heapq.heappop(q)
    ele2 = heapq.heappop(q)
    result += (ele1+ele2)
    heapq.heappush(q,ele1+ele2)

print(result)
