N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

result = 0
for i in range(len(score)-1,0,-1):
    if(score[i]<=score[i-1]):
        result=result+(score[i-1]-(score[i]-1))
        score[i-1]=score[i]-1

print(result)