array=[]
N= int(input())

for _ in range(N):
    array.append(list(map(int,input().split())))
    
compare_idx=[N-1 for i in range(N)]
result=[]

for i in range(N):
    compare_value=[]
    for j in range(N):
        compare_value.append(array[compare_idx[j]][j])
    max_value=max(compare_value)
    result.append(max_value)
    max_idx=compare_value.index(max_value)
    compare_idx[max_idx]-=1

print(result[-1])