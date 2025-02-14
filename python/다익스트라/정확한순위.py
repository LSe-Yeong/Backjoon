N, M = map(int,input().split())
INF = 10e9

score = [[INF for _ in range(N)] for i in range(N)]
for r in range(N):
    score[r][r] = 0

for _ in range(M):
    a,b = map(int,input().split())
    score[a-1][b-1] = 1
    
for k in range(N):
    for r in range(N):
        for c in range(N):
            score[r][c] = min(score[r][c],score[r][k]+score[k][c])

count=0
for i in range(N):
    isPoss = True
    for j in range(N):
        if(score[i][j]==INF and score[j][i]==INF):
            isPoss=False
            break
    if(isPoss):
        count+=1

print(count)
        