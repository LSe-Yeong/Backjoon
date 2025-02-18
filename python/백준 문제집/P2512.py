def cal_cost(costs,mid):
    sum=0
    for v in costs:
        if(v>mid):
            sum+=mid
        else:
            sum+=v
    return sum

def binary(costs,left,right,M):
    mid = 10e10
    result = 10e10
    while left<=right:
        mid = (left+right) // 2
        costs_sum = cal_cost(costs,mid)
        if(costs_sum==M):
            result = mid
            return mid
        
        elif(costs_sum > M):
            right=mid-1
        
        else:
            left=mid+1
            result = mid
        
    return result
            
        

import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

if(sum(arr)<=M):
    print(max(arr))
else:
    print(binary(arr,0,1000000000,M))

