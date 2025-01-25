N = int(input())

array = list(map(int,input().split()))

array.sort()

t =  1
for x in array:
    if t<x:
        break
    t+=x

print(t)