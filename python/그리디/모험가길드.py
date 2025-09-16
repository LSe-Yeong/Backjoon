# #작은놈 부터?

# N = int(input())
# array = list(map(int,input().split()))

# array.sort()

# count=0
# num=0

# for value in array:
#     num+=1
#     if num >= value:
#         count+=1
#         num=0

# print(count)

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

count = 0
group = 0
for i in range(len(arr)):
    count += 1 
    if arr[i] <= count:
        group+=1
        count=0
print(group)





