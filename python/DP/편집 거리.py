str1=input()
str2=input()

N = min(len(str1),len(str2))

DP=[[0 for _ in range(len(str2)+1)] for i in range(len(str1)+1)]
DP[0][0] = (0 if str1[0]==str2[0] else 1)

for r in range(N):
    if(str1[r]==str2[r]):
        DP[r][r] = DP[r-1][r-1]
    else:
        DP[r][r] = DP[r-1][r-1]+1

for r in range(1,len(str1)+1):
    DP[r][0] = DP[r-1][0] + 1

for c in range(1,len(str2)+1):
    DP[0][c] = DP[0][c-1] + 1


for r in range(1,len(str1)):
    for c in range(1,len(str2)):
        if(str1[r]==str2[c]):
            DP[r][c]=DP[r-1][c-1]
        else:
            DP[r][c] = 1 + min(DP[r-1][c],DP[r][c-1],DP[r-1][c-1])

print(DP[len(str1)-1][len(str2)-1])
