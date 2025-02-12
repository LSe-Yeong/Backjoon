import bisect

N, K = map(int,input().split())
array = list(map(int,input().split()))

left = bisect.bisect_left(array,K)
right = bisect.bisect_right(array,K)

diff = right-left

if(diff==0):
    print(-1)
else:
    print(diff)