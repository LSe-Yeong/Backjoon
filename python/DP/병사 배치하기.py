N = int(input())
array = list(map(int,input().split()))

DP = [0 for i in range(N)]
# DP[-1] = 1

# for i in range(N-2,-1,-1):
#     max_v=0
#     for j in range(i+1,N):
#         if(array[i]>array[j] and DP[j]>max_v):
#             max_v = DP[j]
#     DP[i]= max_v + 1
    
    
# print(N-max(DP))

for i in range(N):
    DP[i]=1
    for j in range(0,i):
        if(array[i]<array[j] and DP[j]+1 > DP[i]):
            DP[i]=DP[j] +1
print(DP)