# T = int(input())

# for _ in range(T):
#     my_map=[]
#     N, M = map(int,input().split())
#     array = list(map(int,input().split()))
#     idx=0
#     for i in range(N):
#         my_map.append(array[idx:idx+M])
#         idx+=M
        
#     DP=[[0 for _ in range(M)] for i in range(N)]
#     for r in range(N):
#         DP[r][0]=my_map[r][0]
    
#     for c in range(1,M):
#         for r in range(N):
#             if r==0:
#                 DP[r][c] = max(DP[r+1][c-1],DP[r][c-1])+ my_map[r][c]
#             elif r==N-1:
#                 DP[r][c] = max(DP[r-1][c-1],DP[r][c-1])+ my_map[r][c]
#             else:   
#                 DP[r][c] = max(DP[r+1][c-1],DP[r][c-1],DP[r-1][c-1])+ my_map[r][c]
    
#     max_v = -10e9
#     for i in range(N):
#         if(DP[i][M-1]>max_v):
#             max_v=DP[i][M-1]
#     print(max_v)

# T = int(input())

# for _ in range(T):
#     my_map=[]
#     N, M = map(int,input().split())
#     DP = [[0 for _ in range(M)] for i in range(N)]
#     array = list(map(int,input().split()))
#     idx = 0
#     for r in range(N):
#         my_map.append(array[idx:idx+M])
#         idx += M
#     for r in range(N):
#         DP[r][0] = my_map[r][0]
#     for c in range(1,M):
#         for r in range(N):
#             if r==0:
#                 DP[r][c] = max(DP[r][c-1],DP[r+1][c-1])+my_map[r][c]
#             elif r==N-1:
#                 DP[r][c] = max(DP[r][c-1],DP[r-1][c-1])+my_map[r][c]
#             else:
#                 DP[r][c] = max(DP[r][c-1],DP[r-1][c-1],DP[r+1][c-1])+my_map[r][c]
#     result = -10e9
#     for r in range(N):
#         result = max(DP[r][M-1],result)
#     print(result)
    

def process(r,c):
    if DP[r][c] != -1:
        return DP[r][c]
    
    if c==0:
        DP[r][c] = my_map[r][c]
        return DP[r][c]
    
    if r==0:
        DP[r][c] = max(process(r,c-1),process(r+1,c-1)) + my_map[r][c]
    elif r==N-1:
        DP[r][c] = max(process(r,c-1),process(r-1,c-1)) + my_map[r][c]
    else:
        DP[r][c] = max(process(r,c-1),process(r-1,c-1),process(r+1,c-1)) + my_map[r][c]
    return DP[r][c]

T = int(input())

for _ in range(T):
    my_map=[]
    N, M = map(int,input().split())
    DP = [[-1 for _ in range(M)] for i in range(N)]
    array = list(map(int,input().split()))
    idx = 0
    for r in range(N):
        my_map.append(array[idx:idx+M])
        idx += M
    
    for r in range(N):
        DP[r][0] = my_map[r][0]
    
    result = -10e9
    for r in range(N):
        value = process(r,M-1)
        print(value)
        result = max(result,value)
    
    
    