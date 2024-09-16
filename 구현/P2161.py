from collections import deque

queue=deque()
result=[]

N=int(input())

for i in range(1,N+1):
    queue.append(i)

while queue:
    element=queue.popleft()
    result.append(element)
    if queue:
        queue.append(queue.popleft())
        
for i in range(len(result)):
    print(result[i], end=" ")