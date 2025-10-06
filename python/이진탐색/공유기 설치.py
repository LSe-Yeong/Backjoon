# N, C = map(int,input().split())
# array = []
# for _ in range(N):
#     array.append(int(input()))
# array.sort()
# result=0

# def b_s(arr,start,end):
#     while start<=end:
#         mid = (start+end)//2
        
#         now = arr[0]
#         count=1
        
#         for i in range(N):
#             if(arr[i]>=mid+now):
#                 count+=1
#                 now = arr[i]
                
#         global result
#         if(count>=C):
#             result=mid
#             start=mid+1
#         else:
#             end=mid-1

# b_s(array,1,array[-1]-array[0])
# print(result)

N,C = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

left = 1
right = arr[-1] - arr[0]
result = -10e9

while left<=right:
    mid = (left+right)//2
    count_share = 1
    now = arr[0]
    for i in range(1,N):
        if arr[i] - now >= mid:
            count_share+=1
            now = arr[i]
    if count_share >= C:
        result = max(result,mid)
        left = mid + 1
    else:
        right = mid - 1

print(result)
