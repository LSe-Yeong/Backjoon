N=int(input())
hour,min,second=0,0,0
count=0

while True:
    if(hour==N+1):
        break
    second=second+1
    if(second==60):
        min=min+1
        second=0
    if(min==60):
        hour=hour+1
        min=0
    time=str(hour)+str(min)+str(second)
    if '3' in time:
        count=count+1
print(count)