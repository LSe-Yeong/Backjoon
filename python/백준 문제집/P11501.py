def solution(arr):
    max_v = -10e9
    total = 0
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]>max_v):
            max_v = arr[i]
        else:
            total+=(max_v - arr[i])
            
    return total

import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    array = list(map(int,sys.stdin.readline().split()))
    s = solution(array)
    print(s)