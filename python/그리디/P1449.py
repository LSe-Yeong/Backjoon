N,L = map(int,input().split())
array = list(map(int,input().split()))
array.sort()

idx=0
isFinish = False
count=0
while True:
    start = array[idx]-0.5
    end = start + L
    count+=1
    while array[idx]+0.5 <= end:
        idx+=1
        if(idx==len(array)):
            isFinish=True
            break
    if(isFinish):
        break

print(count)
    