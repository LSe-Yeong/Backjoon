def rotate_90_clockwise(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]
                            
def solution(key, lock):
    n = len(key)
    m = len(lock)
    wide_lock = [[0 for _ in range(m * 3)] for i in range(m * 3)]
    for i in range(m):
        for j in range(m):
            wide_lock[i+m][j+m] = lock[i][j]
    
    for _ in range(4):
        key = rotate_90_clockwise(key)
        for i in range(0,2*m):
            for j in range(0,2*m):
                for r in range(n):
                    for c in range(n):
                        wide_lock[i+r][j+c] += key[r][c]
                isEnable=True
                for r in range(m):
                    for c in range(m):
                        if(wide_lock[r+m][c+m]!=1):
                            isEnable=False
                if(isEnable):
                    return True
                else:
                    for r in range(n):
                        for c in range(n):
                            wide_lock[i+r][j+c] -= key[r][c]                        
    return False
