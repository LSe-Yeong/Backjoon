from bisect import bisect_left, bisect_right

N,X=map(int,input().split())

array=list(map(int,input().split()))

left_idx=bisect_left(array,X)
right_idx=bisect_right(array,X)

if right_idx-left_idx==0:
    print(-1)
else:
    print(right_idx-left_idx)