import heapq

N = int(input())

schedules = []

for _ in range(N):
    start,end = map(int,input().split())
    schedules.append((start,end))

schedules.sort()

queue=[]
heapq.heappush(queue,schedules[0][1])
count=1

for i in range(1,len(schedules)):
    fastest_time = queue[0]
    time_start = schedules[i][0]
    time_end = schedules[i][1]
    if time_start < fastest_time:
        heapq.heappush(queue,time_end)
        count+=1
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,time_end)

print(count)

      
