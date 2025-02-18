def insert_x(arr,x):
    if len(arr)==0:
        arr.append(x)
        return 0
    
    result = 0
    for i in range(len(arr)):
        if arr[i] > x:
            result += (len(arr)-i)
            arr.insert(i,x)
            return result
        
    arr.append(x)
    return result

import sys

P = int(sys.stdin.readline())

for _ in range(P):
    arr = list(map(int,sys.stdin.readline().split()))
    result = []
    total = 0
    
    for x in arr[1:]:
        total += insert_x(result,x)
    
    print(_+1,end=" ")
    print(total)
