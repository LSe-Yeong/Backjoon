def find1(n):
    if DP[n] != 0:
        return DP[n]
    if n%3==0 and n%2==0:
        DP[n] = min(find1(n//3),find1(n//2),find1(n-1))+1
    elif n%3==0:
        DP[n] = min(find1(n//3),find1(n-1))+1
    elif n%2==0:
        DP[n] = min(find1(n//2),find1(n-1))+1
    else:
        DP[n] = find1(n-1) + 1
    return DP[n]

N = int(input())

DP = [0 for i in range(N+1)]
if N==1:
    print(0)
elif N==2:
    print(1)
elif N==3:
    print(1)
else:
    DP[2] = 1
    DP[3] = 1
    print(find1(N))