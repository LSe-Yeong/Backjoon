N,M,K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

result = 0
idx = 0
while idx<M:
    for i in range(K):
        
        result+=arr[-1]
        idx+=1
        if idx == M:
            break
    if idx == M:
        break
    result+=arr[-2]
    idx+=1

print(result)