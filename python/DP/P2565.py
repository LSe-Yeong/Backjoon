N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
DP = [0 for i in range(N)]

arr.sort()

DP[0] = 1

for i in range(N):
    DP[i] = 1
    for j in range(i):
        if arr[j][1] <= arr[i][1] and DP[i] < DP[j] + 1:
            DP[i] = DP[j] + 1
            
print(N-max(DP))
