# N=int(input())
# M=int(input())
# X=list(map(int,input().split()))
# result=[]

# def isLightAll(h):
#     ddang=set(list(range(0,N)))
#     for i in range(len(X)):
#         ddang -= set(list(range(X[i]-h,X[i]+h)))
#     if ddang:
#         return False
#     else:
#         return True

# left=0
# right=N

# while left<=right:
#     mid = (left+right)//2
#     if isLightAll(mid):
#         result.append(mid)
#         right=mid-1
#     elif not isLightAll(mid):
#         left=mid+1

# print(min(result))


N=int(input())
M=int(input())
X=list(map(int,input().split()))
result=[]

height=X[0]
for i in range(1,M):
    distance=X[i]-X[i-1]
    if(distance%2==0):
        height=max(height,distance//2)
    else:
        height=max(height,(distance//2)+1)
print(max(height,N-X[M-1]))

    
    