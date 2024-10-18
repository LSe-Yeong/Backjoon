from collections import deque

game=[0 for _ in range(101)]

def bfs(start):
    queue=deque()
    dice=[1,2,3,4,5,6]
    game[1]=1
    queue.append(start)
    while queue:
        ele = queue.popleft()
        for i in range(len(dice)):
            nSpot=ele+dice[i]
            for i in range(len(rope)):
                if nSpot == rope[i][0]:
                    nSpot = rope[i][1]
            for i in range(len(snake)):
                if nSpot == snake[i][0]:
                    nSpot = snake[i][1]
            if(nSpot>100):
                continue
            if(game[nSpot]==0):
                game[nSpot]=game[ele]+1
                queue.append(nSpot)
                
snake=[]
rope=[]

N, M = map(int,input().split())

for _ in range(N):
    rope.append(list(map(int,input().split())))

for _ in range(M):
    snake.append(list(map(int,input().split())))

start=1
bfs(start)

print(game[100]-1)