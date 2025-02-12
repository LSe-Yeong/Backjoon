import bisect

N, K = map(int,input().split())
array = list(map(int,input().split()))


## bisect 방법
# left = bisect.bisect_left(array,K)
# right = bisect.bisect_right(array,K)

# diff = right-left

# if(diff==0):
#     print(-1)
# else:
#     print(diff)

def first(arr,k,left,right):
    if(left>right):
        return None
    mid = (left+right)//2
    if((mid==0 or k>arr[mid-1]) and arr[mid]==k):
        return mid
    elif(arr[mid]>=k):
        return first(arr,k,left,mid-1)
    else:
        return first(arr,k,mid+1,right)

def last(arr,k,left,right):
    if(left>right):
        return None
    mid = (left+right)//2
    if((mid==N-1 or k<arr[mid+1]) and arr[mid]==k):
        return mid
    elif(arr[mid]>k):
        return last(arr,k,left,mid-1)
    else:
        return last(arr,k,mid+1,right)

