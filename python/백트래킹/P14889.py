def cal_score(member):
    score = 0
    for r in member:
        for c in member:
            score += arr[r][c]
    return score

def backT(idx):
    global result
    if len(teamA) == K:
        teamB = set()
        for i in range(N):
            if i not in teamA:
                teamB.add(i)

        a = cal_score(teamA)
        b = cal_score(teamB)
        result = min(result,abs(a-b))
        return
    
    for i in range(idx,N):
        teamA.add(i)
        backT(i+1) 
        teamA.remove(i)

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

K = N // 2
result = 10e15

teamA = set()
backT(0)

print(result)