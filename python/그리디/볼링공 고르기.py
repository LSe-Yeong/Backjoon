N, M = map(int,input().split())
array = list(map(int,input().split()))

# count=0

# for i in range(N):
#     for j in range(i+1,N):
#         if(array[i]!=array[j]):
#             count+=1

# print(count)            

weight = [0 for i in range(M+1)]

for i in range(N):
    weight[array[i]]+=1

result=0
for i in range(1,M):
    N-=weight[i]
    result+=weight[i]*N
    
print(result)