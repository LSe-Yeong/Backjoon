N = int(input())
array = list(map(int,input().split()))

def b_s(arr,start,end):
    if(start>end):
        return None
    mid = (start+end)//2
    if(arr[mid]==mid):
        print(mid)
        return
    elif(arr[mid]>mid):
        b_s(arr,start,mid-1)
    else:
        b_s(arr,mid+1,end)

print(b_s(array,0,N-1))