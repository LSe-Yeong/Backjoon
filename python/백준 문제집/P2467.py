from bisect import bisect_right

N = int(input())
array = list(map(int,input().split()))
array.sort()
mixed_v = 0
result=10e15
answer = []
selected_target = 0

for i in range(len(array)):
    target = -array[i]
    print(target)
    idx = bisect_right(array,target)    
    if(idx==len(array)):
        mixed_v = array[i] + array[idx-1]
        selected_target = idx-1
    elif(idx==0):
        mixed_v = array[i] + array[idx]
        selected_target = idx
    else:
        abs1 = abs(array[i]+array[idx-1])
        abs2 = abs(array[i]+array[idx])
        if(abs1>abs2):
            mixed_v = array[i] + array[idx]
            selected_target = idx
        else:
            mixed_v = array[i] + array[idx-1]
            selected_target = idx-1
    
    if(selected_target == i):
        continue

    if(abs(result)>abs(mixed_v)):
        result = mixed_v
        answer = [array[i],array[selected_target]]

answer.sort()    
for v in answer:
    print(v, end=" ")
        


