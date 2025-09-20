# def rotate_90_clockwise(matrix):
#     return [list(reversed(col)) for col in zip(*matrix)]
                            
# def solution(key, lock):
#     n = len(key)
#     m = len(lock)
#     wide_lock = [[0 for _ in range(m * 3)] for i in range(m * 3)]
#     for i in range(m):
#         for j in range(m):
#             wide_lock[i+m][j+m] = lock[i][j]
    
#     for _ in range(4):
#         key = rotate_90_clockwise(key)
#         for i in range(0,2*m):
#             for j in range(0,2*m):
#                 for r in range(n):
#                     for c in range(n):
#                         wide_lock[i+r][j+c] += key[r][c]
#                 isEnable=True
#                 for r in range(m):
#                     for c in range(m):
#                         if(wide_lock[r+m][c+m]!=1):
#                             isEnable=False
#                 if(isEnable):
#                     return True
#                 else:
#                     for r in range(n):
#                         for c in range(n):
#                             wide_lock[i+r][j+c] -= key[r][c]                        
#     return False

def rotate_90_clockwise(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def isEnabled(w_m,N):
    for r in range(N,2*N):
        for c in range(N,N*2):
            if(w_m[r][c]!=1):
                return False
    return True

def solution(key,lock):
    M = len(key)
    N = len(lock)
    wide_map = [[0 for _ in range(N*3)] for i in range(N*3)]

    for i in range(N,N*2):
        for j in range(N,N*2):
            wide_map[i][j] = lock[i-N][j-N]

    for _ in range(4):
        key = rotate_90_clockwise(key)
        for i in range(0,2*N):
            for j in range(0,2*N):
                for r in range(M):
                    for c in range(M):
                        wide_map[i+r][j+c] += key[r][c]
                if(isEnabled(wide_map,N)):
                    return True
                else:
                    for r in range(M):
                        for c in range(M):
                            wide_map[i+r][j+c] -= key[r][c]
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))