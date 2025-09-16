# N = int(input())

# array = list(map(int,input().split()))

# array.sort()

# t =  1
# for x in array:
#     if t<x:
#         break
#     t+=x

# print(t)

# 1 1 4(1,2,3중 하나) => 3
# 1 1 3 (1,2,3,4,5,6 중 하나)=> 5원 가능
# 1 1 5 => 3 

N = int(input())
arr = list(map(int,input().split()))

arr.sort()

v = 1

for i in range(len(arr)):
    if v < arr[i]:
        break
    v+=arr[i]

print(v)


