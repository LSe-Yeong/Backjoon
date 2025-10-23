N,K = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = K - 1

sum_now = sum(arr[left:right+1])
result = sum_now
while right < len(arr)-1:
    left += 1
    right += 1
    sum_now = sum_now + arr[right]
    sum_now = sum_now - arr[left-1]
    result = max(sum_now,result)

print(result)


