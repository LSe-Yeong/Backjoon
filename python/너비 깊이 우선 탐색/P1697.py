from collections import deque
N, K=map(int,input().split())

my_map=[-1 for _ in range(100001)]

queue=deque()

my_map[N]=0
queue.append([N, my_map[N]])
while queue:
    ele = queue.popleft()
    idx = ele[0]
    min_count= ele[1]

    if(idx-1>=0 and my_map[idx-1]==-1):
        my_map[idx-1]=min_count+1
        queue.append([idx-1,my_map[idx-1]])
    if(idx+1<=100000 and my_map[idx+1]==-1):
        my_map[idx+1]=min_count+1
        queue.append([idx+1,my_map[idx+1]])
    if(idx*2<=100000 and my_map[idx*2]==-1):
        my_map[idx*2]=min_count+1
        queue.append([idx*2, my_map[idx*2]])

print(my_map[K])