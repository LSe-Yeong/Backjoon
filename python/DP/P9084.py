T = int(input())

for t in range(T):
    N = int(input())
    coins = list(map(int,input().split()))
    target = int(input())
    DP = [0 for i in range(target+1)]
    DP[0] = 1
    for coin in coins:
        for i in range(1,target+1):
            if i-coin >= 0:
                DP[i] += DP[i-coin] 

    print(DP[target])

