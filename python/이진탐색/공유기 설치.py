N, C = map(int,input().split())
array = []
for _ in range(N):
    array.append(int(input()))
array.sort()
result=0

def b_s(arr,start,end):
    while start<=end:
        mid = (start+end)//2
        
        now = arr[0]
        count=1
        
        for i in range(N):
            if(arr[i]>=mid+now):
                count+=1
                now = arr[i]
                
        global result
        if(count>=C):
            result=mid
            start=mid+1
        else:
            end=mid-1

b_s(array,1,array[-1]-array[0])
print(result)