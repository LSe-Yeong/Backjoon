T = int(input())

for _ in range(T):
    my_map=[]
    N, M = map(int,input().split())
    array = list(map(int,input().split()))
    idx=0
    for i in range(N):
        my_map.append(array[idx:idx+M])
        idx+=M
        
    DP=[[0 for _ in range(M)] for i in range(N)]
    for r in range(N):
        DP[r][0]=my_map[r][0]
    
    for c in range(1,M):
        for r in range(N):
            if r==0:
                DP[r][c] = max(DP[r+1][c-1],DP[r][c-1])+ my_map[r][c]
            elif r==N-1:
                DP[r][c] = max(DP[r-1][c-1],DP[r][c-1])+ my_map[r][c]
            else:   
                DP[r][c] = max(DP[r+1][c-1],DP[r][c-1],DP[r-1][c-1])+ my_map[r][c]
    
    max_v = -10e9
    for i in range(N):
        if(DP[i][M-1]>max_v):
            max_v=DP[i][M-1]
    print(max_v)