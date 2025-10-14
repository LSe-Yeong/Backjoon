# N = int(input())

# array=[]

# for _ in range(N):
#     array.append(list(map(int,input().split())))

# for r in range(1,N):
#     for c in range(len(array[r])):
#         if c == 0:
#             array[r][c] = array[r][c] + array[r-1][c]
#         elif c== len(array[r])-1:
#             array[r][c] = array[r][c] + array[r-1][c-1]
#         else:
#             array[r][c] = array[r][c] + max(array[r-1][c],array[r-1][c-1])

# print(max(array[-1]))

# N = int(input())

# array=[]

# for _ in range(N):
#     array.append(list(map(int,input().split())))

# DP = [[0 for i in range(j+1)] for j in range(N)]

# DP[0][0] = array[0][0]

# for r in range(1,len(DP)):
#     for c in range(len(DP[r])):
#         if c==0:
#             DP[r][c] = DP[r-1][c] + array[r][c]
#         elif c==len(DP[r])-1:
#             DP[r][c] = DP[r-1][c-1] + array[r][c]
#         else:
#             DP[r][c] = max(DP[r-1][c],DP[r-1][c-1]) + array[r][c]
# print(max(DP[-1]))

def topDown(r,c):
    if DP[r][c] != -1:
        return DP[r][c]
    
    if r==0:
        return array[r][0]

    if c==0:
        DP[r][c] = topDown(r-1,c) + array[r][c]
        return DP[r][c]
    elif c==len(DP[r])-1:
        DP[r][c] = topDown(r-1,c-1) + array[r][c]
        return DP[r][c]
    else:
        DP[r][c] = max(topDown(r-1,c-1),topDown(r-1,c)) + array[r][c]
        return DP[r][c]

N = int(input())

array=[]

for _ in range(N):
    array.append(list(map(int,input().split())))
result = []
DP = [[-1 for i in range(j+1)] for j in range(N)]

for i in range(N):
    result.append(topDown(N-1,i))
    
print(max(result))


