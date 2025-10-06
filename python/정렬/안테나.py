# N = int(input())

# array = list(map(int,input().split()))

# array.sort()

# print(array[(len(array)-1)//2])

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[(len(arr)-1)//2])