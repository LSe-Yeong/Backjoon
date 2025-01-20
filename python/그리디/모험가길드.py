#작은놈 부터?

N = int(input())
array = list(map(int,input().split()))

array.sort()

count=0
num=0

for value in array:
    num+=1
    if num >= value:
        count+=1
        num=0

print(count)