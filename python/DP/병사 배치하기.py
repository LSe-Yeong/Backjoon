# N = int(input())
# array = list(map(int,input().split()))

# DP = [0 for i in range(N)]
# DP[-1] = 1

# ## 방법 1
# for i in range(N-2,-1,-1):
#     max_v=0
#     for j in range(i+1,N):
#         if(array[i]>array[j] and DP[j]>max_v):
#             max_v = DP[j]
#     DP[i]= max_v + 1
    
    
# print(N-max(DP))


# ## 방법 2
# for i in range(N):
#     DP[i]=1
#     for j in range(0,i):
#         if(array[i]<array[j] and DP[j]+1 > DP[i]):
#             DP[i]=DP[j] +1
# print(DP)

# N = int(input())
# arr = list(map(int,input().split()))
# DP = [0 for i in range(N)]

# for i in range(N-1,-1,-1):
#     DP[i] = 1
#     for j in range(i+1,N):
#         if arr[j] < arr[i] and DP[j]+1 > DP[i]:
#             DP[i] = DP[j] + 1

# if N==1:
#     print(0)
# else:
#     print(N-max(DP))

def LCS(n):
    if DP[n] != 1:
        return DP[n]
    
    for i in range(n+1,N):
        if arr[n] > arr[i]:
            DP[n] = max(LCS(i)+1,DP[n])
    
    return DP[n]
    

N = int(input())
arr = list(map(int,input().split()))
DP = [1 for i in range(N)]

print(N-max(DP))
