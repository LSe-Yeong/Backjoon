# def one_move(snake_state,t):
#     global this_command,this_command_idx,snake_state1
#     if(snake_rotate[snake_state]=="R"):
#         snake.append((snake[-1][0],snake[-1][1]+1))
#     if(snake_rotate[snake_state]=="B"):
#         snake.append((snake[-1][0]+1,snake[-1][1]))
#     if(snake_rotate[snake_state]=="L"):
#         snake.append((snake[-1][0],snake[-1][1]-1))
#     if(snake_rotate[snake_state]=="T"):
#         snake.append((snake[-1][0]-1,snake[-1][1]))
    
#     #충돌 확인
#     for i in range(len(snake)-1):
#         value = snake[i]
#         i,j = value
#         if(snake[-1][0]==i and snake[-1][1]==j):
#             return t
#     if(snake[-1][0]<0 or snake[-1][0]>N-1 or snake[-1][1]<0 or snake[-1][1]>N-1):
#         return t
    
#     #사과
#     if(my_map[snake[-1][0]][snake[-1][1]]!=1):
#         snake.pop(0)
#     else:
#         my_map[snake[-1][0]][snake[-1][1]]=0
    
#     #회전
#     if(this_command[0]==t):
#         if(this_command[1]=="D"):
#             snake_state1=(snake_state1+1)%4
#         else:
#             snake_state1=(snake_state1-1)%4
#         this_command_idx+=1
#         if(this_command_idx<len(command)):
#             this_command=command[this_command_idx]
#     return 400
    
# N = int(input())
# my_map = [[0 for _ in range(N)] for i in range(N)]
# snake = [(0,0)]
# snake_rotate=["R","B","L","T"]
# snake_state1 = 0
# command = []
# this_command = 0
# this_command_idx=0

# K = int(input())
# for _ in range(K):
#     i, j = map(int,input().split())
#     my_map[i-1][j-1]=1
    
# L = int(input())
# for _ in range(L):
#     X, rotate = map(str,input().split())
#     X=int(X)
#     command.append((X,rotate))
# this_command=command[0]

# i=1
# while(True):
#     num = one_move(snake_state1,i)
#     if(num!=400):
#         print(num)
#         break
#     i+=1

from collections import deque

def isEnd(board,head,tail,snakeLog):
    N = len(board)
    if head in snakeLog:
        return True
    for i in range(2):
        if head[i] > N-1 or head[i] < 0:
            return True
    return False
    


d_g = [(0,1),(1,0),(0,-1),(-1,0)]
now_dir = 0
change_dir = []
change_time = set()
snakeLog = deque()

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for i in range(N)]
for i in range(K):
    r,c = map(int,input().split())
    board[r-1][c-1] = 1
L = int(input())
for i in range(L):
    X,C = input().split()
    X = int(X)
    change_dir.append((X,C))
    change_time.add(X)

time = 0
head = [0,0]
tail = [0,0]
snakeLog.append([0,0])
while True:
    for i in range(2):
        head[i]+=d_g[now_dir][i]
    if(isEnd(board,head,tail,snakeLog)):
        break
    snakeLog.append([head[0],head[1]])
    if board[head[0]][head[1]]==1:
        board[head[0]][head[1]] = 0
    else:
        snakeLog.popleft()
    time += 1
    print(snakeLog)
    for i in range(len(change_dir)):
        if change_dir[i][0] == time:
            if change_dir[i][1] == 'L':
                now_dir = (now_dir-1) % 4
            else:
                now_dir = (now_dir+1) % 4
    
print(time+1)



