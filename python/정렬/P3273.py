N=int(input())
numbers=list(map(int,input().split()))
x=int(input())

numbers.sort()

left,right=0,N-1
count=0

while(left<right):
    ele=numbers[left]+numbers[right]
    if ele<x:
        left+=1
    elif ele>x:
        right-=1
    else:
        count+=1
        left+=1
        
print(count)
        