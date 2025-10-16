N = int(input())
K = int(input())
arr = list(map(int,input().split()))
arr.sort()
distance = [0 for _ in range(N-1)]
for i in range(1,len(arr)):
    distance[i-1] = arr[i] - arr[i-1]
distance.sort(reverse=True)

print(sum(distance[K-1:]))