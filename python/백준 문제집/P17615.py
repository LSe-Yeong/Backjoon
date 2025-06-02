import sys

N = int(sys.stdin.readline())
balls = sys.stdin.readline()
result=[]
colors=["R","B"]

for color in colors:
    start=False
    count=0
    for i in range(N-1,-1,-1):
        if(balls[i]!=color):
            start=True
            
        if(start and balls[i]==color):
           count+=1
           
    result.append(count)

print(min(result))         

