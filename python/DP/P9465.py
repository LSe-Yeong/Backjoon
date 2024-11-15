T = int(input())

for _ in range(T):
    sticker = []
    N = int(input())
    DP=[[0 for i in range(N)] for j in range(2)]
    for i in range(2):
        sticker.append(list(map(int,input().split())))
        
    if(N==1):
        print(max(sticker[0][0],sticker[1][0]))
    elif(N==2):
        print(max(sticker[1][0]+sticker[0][1],sticker[1][1]+sticker[0][0]))
    else:
        DP[0][0]=sticker[0][0]
        DP[1][0]=sticker[1][0]
        DP[0][1]=sticker[1][0]+sticker[0][1]
        DP[1][1]=sticker[0][0]+sticker[1][1]
        
        for i in range(2,N):
            DP[0][i] = max(DP[1][i-1],DP[1][i-2])+sticker[0][i]
            DP[1][i] = max(DP[0][i-1],DP[0][i-2])+sticker[1][i]
        
        max_value=0
        for i in range(2):
            max_temp=max(DP[i])
            if(max_temp>max_value):
                max_value=max_temp
        print(max_value)
        