def batch(idx,k):
    cnt=0
    i=0
    while True:
        if(cnt==k and result[i]==0):
            result[i]=idx
            break
        
        if(result[i]==0):
            cnt+=1
        
        i+=1
        
    return
    
import sys

N = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
result = [0 for i in range(N)]

for i in range(1,N+1):
    batch(i,array[i-1])

for v in result:
    print(v, end=" ")
    
