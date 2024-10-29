N=int(input())
arr=list(map(int,input().split()))
DP=[0 for _ in range(N)]

for i in range(len(arr)):
    DP[i]=1
    for j in range(0,i):
        if(arr[j]<arr[i] and DP[j]+1>DP[i]):
            DP[i]=DP[j]+1

print(max(DP))

# N=int(input())
# arr=list(map(int,input().split()))
# DP=[0 for _ in range(N)]

# for i in range(len(arr)):
#     DP[i]=1
#     DP_buffer=[1]
#     for j in range(0,i):
#         if(arr[j]<arr[i]):
#             DP_buffer.append(DP[j]+1)
#     DP[i]=max(DP_buffer)

# print(max(DP))