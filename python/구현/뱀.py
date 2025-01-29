def one_move(snake_state,t):
    global this_command,this_command_idx,snake_state1
    if(snake_rotate[snake_state]=="R"):
        snake.append((snake[-1][0],snake[-1][1]+1))
    if(snake_rotate[snake_state]=="B"):
        snake.append((snake[-1][0]+1,snake[-1][1]))
    if(snake_rotate[snake_state]=="L"):
        snake.append((snake[-1][0],snake[-1][1]-1))
    if(snake_rotate[snake_state]=="T"):
        snake.append((snake[-1][0]-1,snake[-1][1]))
    
    #충돌 확인
    for i in range(len(snake)-1):
        value = snake[i]
        i,j = value
        if(snake[-1][0]==i and snake[-1][1]==j):
            return t
    if(snake[-1][0]<0 or snake[-1][0]>N-1 or snake[-1][1]<0 or snake[-1][1]>N-1):
        return t
    
    #사과
    if(my_map[snake[-1][0]][snake[-1][1]]!=1):
        snake.pop(0)
    else:
        my_map[snake[-1][0]][snake[-1][1]]=0
    
    #회전
    if(this_command[0]==t):
        if(this_command[1]=="D"):
            snake_state1=(snake_state1+1)%4
        else:
            snake_state1=(snake_state1-1)%4
        this_command_idx+=1
        if(this_command_idx<len(command)):
            this_command=command[this_command_idx]
    return 400
    
N = int(input())
my_map = [[0 for _ in range(N)] for i in range(N)]
snake = [(0,0)]
snake_rotate=["R","B","L","T"]
snake_state1 = 0
command = []
this_command = 0
this_command_idx=0

K = int(input())
for _ in range(K):
    i, j = map(int,input().split())
    my_map[i-1][j-1]=1
    
L = int(input())
for _ in range(L):
    X, rotate = map(str,input().split())
    X=int(X)
    command.append((X,rotate))
this_command=command[0]

i=1
while(True):
    num = one_move(snake_state1,i)
    if(num!=400):
        print(num)
        break
    i+=1

