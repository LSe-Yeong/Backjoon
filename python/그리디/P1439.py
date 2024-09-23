array=list(input())
count=[0,0]

for i in range(len(array)):
    if(array[i]!=array[i-1]):
        count[int(array[i-1])]+=1
if(array[-1]!=array[-2]):
    count[int(array[-1])]+=1
    
print(min(count))
    