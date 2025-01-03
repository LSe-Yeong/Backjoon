X = int(input())

DP = [0 for _ in range(30001)]

for i in range(2,X+1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i],DP[i//2]+1)
    elif i % 3 == 0:
        DP[i] = min(DP[i],DP[i//3]+1) 
    elif i % 5 == 0:
        DP[i] = min(DP[i],DP[i//5]+1) 

print(DP[X])