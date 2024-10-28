N=int(input())
times=[]
pays=[]

DP = [0 for _ in range(N+1)]

for i in range(N):
    time,pay=map(int,input().split())
    times.append(time)
    pays.append(pay)

for i in range(N):
    print(DP)
    for j in range(i+times[i],N+1):
        if DP[j] < DP[i] + pays[i]:
            DP[j] = DP[i] + pays[i]
