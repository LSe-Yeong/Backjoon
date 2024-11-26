N, S = map(int,input().split())

array = list(map(int,input().split()))

left = 0
right = 0
sum=array[0]
INF=10e9
length=INF

while(True):
    if(left>N-1 or right>N-1 or left>right):
        break
    if(sum>=S):
        if(right-left<length):
            length=right-left+1
        sum-=array[left]
        left+=1
    elif(sum<S):
        right+=1
        if(right<N):
            sum+=array[right]
if(length==INF):
    print(0)
else:
    print(length)        
        
    