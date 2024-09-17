N=int(input())
M=int(input())
X=list(map(int,input().split()))
result=[]

def isLightAll(h):
    ddang=set(list(range(0,N)))
    for i in range(len(X)):
        ddang -= set(list(range(X[i]-h,X[i]+h)))
    if ddang:
        return False
    else:
        return True

left=0
right=N

while left<=right:
    mid = (left+right)//2
    if isLightAll(mid):
        result.append(mid)
        right=mid-1
    elif not isLightAll(mid):
        left=mid+1

print(min(result))

    
    