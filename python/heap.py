import heapq

max_heap=[]

heapq.heappush(max_heap,(-4,5))
heapq.heappush(max_heap,(-9,5))
heapq.heappush(max_heap,(-7,4))
heapq.heappush(max_heap,(-2,8))
heapq.heappush(max_heap,(-10,9))
heapq.heappush(max_heap,(-8,1))

print(max_heap)

print(-heapq.heappop(max_heap)[1])
print(-heapq.heappop(max_heap)[1])
print(-heapq.heappop(max_heap)[1])
print(-heapq.heappop(max_heap)[1])
print(-heapq.heappop(max_heap)[1])
print(-heapq.heappop(max_heap)[1])

