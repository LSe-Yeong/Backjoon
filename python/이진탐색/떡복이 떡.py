N,M=map(int,input().split())

array=list(map(int,input().split()))
result=[]
start=0
end=max(array)
mid=0
while start<=end:
    mid = (start+end)//2
    sum=0
    for i in range(0,len(array)):
        if(array[i]-mid>=0):
            sum=sum+array[i]-mid
    if(sum>=M):
        result.append(mid)
        start=mid+1
    else:
        end=mid-1
print(result[-1])