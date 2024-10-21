N, M = map(int,input().split())
board=[]
correct_white=["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
correct_black=["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
correct=[]
for i in range(N):
    board.append(input())

result=10000000

for row in range(N-7):
    for col in range(M-7):
        count=0
        count_black=0
        for i in range(row,row+8):
            for j in range(col,col+8):
                if(correct_black[i-row][j-col]!=board[i][j]):
                    count_black+=1
        count_white=0
        for i in range(row,row+8):
            for j in range(col,col+8):
                if(correct_white[i-row][j-col]!=board[i][j]):
                    count_white+=1
        if(count_black>=count_white):
            count=count_white
        else:
            count=count_black
        if(result>count):
            result=count

print(result)