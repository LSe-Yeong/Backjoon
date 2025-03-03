import sys

N,K = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))
count=[0 for i in range(100001)]

start=0
end=0
count[array[end]]=1
max_length=1

while end < len(array):
    if(count[array[end]]>K):
        while start<end and array[start]!=array[end]:
            count[array[start]]-=1
            start+=1
        count[array[start]]-=1    
        start+=1
    else:
        end+=1
        if(end<len(array)):
            count[array[end]]+=1
    max_length = max(max_length,end-start)

print(max_length)
   
        