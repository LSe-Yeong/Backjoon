def catch_shark(col):
    for r in range(N):
        if len(water[r][col]) != 0:
            size = water[r][col][4]
            water[r][col] = []
            return size
    return 0

def move_shark():
    return 

N,M,S = map(int,input().split())
sharks = []
water = [[[] for i in range(M)] for j in range(N)]
for i in range(S):
    r,c,s,d,z = map(int,input().split())
    water[r-1][c-1] = [s,d,z]

start = -1
result = 0
while start < M-1:
    start += 1
    result += catch_shark(start)
    move_shark()

