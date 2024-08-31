#P18111

'''
아이디어: 
1. 전수 조사 해야할듯 (범위가 그렇게 안 큼)
2. 전수 조사 후 시간의 최소값을 찾음
'''

N,M,B=map(int,input().split())
block_map=[]
block=B
time=[]
height=0

for _ in range(N):
    block_map.append(list(map(int,input().split())))

for h in range(0,257):
    this_time=0
    block=B
    for i in range(N):
        for j in range(M):
            if(block_map[i][j]<h):
                block-=(h-block_map[i][j])
                this_time=this_time+h-block_map[i][j]
            elif(block_map[i][j]>h):
                block+=(block_map[i][j]-h)
                this_time=this_time+2*(block_map[i][j]-h)
    if(block<0):
        break
    time.append(this_time)
    if(time[h]<=time[height]):
        height=h
print(time[height],height)
                
            

