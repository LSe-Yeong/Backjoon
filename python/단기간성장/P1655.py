import heapq,sys

def balance_heap(lower,upper):
    if len(lower) > len(upper)+1:
        heapq.heappush(upper, -1 * heapq.heappop(lower))
    elif len(lower) < len(upper):
        heapq.heappush(lower,-1 * heapq.heappop(upper))
    return -lower[0]

lower = []
upper = []

N = int(input())
mid = 0
for i in range(N):
    num = int(sys.stdin.readline())
    if num <= mid:
        heapq.heappush(lower,-num)
    else:
        heapq.heappush(upper,num)
    mid = balance_heap(lower,upper)
    print(mid)