N = int(input())
array = list(map(int,input().split()))

array.sort()

result=[]

left=0
right=N-1
result = [array[left],array[right]]
min_value = abs(array[left]+array[right])

while(left < right):
    value = array[left] + array[right]
    if(value>0):
        if(abs(value)<min_value):
            min_value = abs(value)
            result = [array[left],array[right]]
        right-=1
    elif(value<0):
        if(abs(value)<min_value):
                min_value = abs(value)
                result = [array[left],array[right]]
        left+=1
    else:
        result = [array[left],array[right]]
        break
        
for i in range(len(result)):
    print(result[i],end=" ")
