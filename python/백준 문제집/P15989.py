max_v = 10001
DP = [1 for _ in range(max_v)]
for i in range(2,max_v):
    DP[i] = DP[i] + DP[i-2]
for i in range(3,max_v):
    DP[i] = DP[i] + DP[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N])

#Test