# N = int(input())
# array=[]

# for _ in range(N):
#     array.append(list(map(int,input().split())))

# DP=[0 for _ in range(N)]

# for i in range(N-1,-1,-1):
#     if(i+array[i][0]==N):
#         DP[i] = array[i][1]
#         continue
#     if(i+array[i][0]>N-1):
#         continue
#     DP[i] = max(DP[i+array[i][0]:N]) + array[i][1]

# print(max(DP))

def topDown(n):
    if max_per_person[n] != 0:
        return max_per_person[n]
    
    if n==0:
        max_per_person[n] = arr[0][1]
        return arr[0][1]
    
    add_p = 0
    for i in range(n-1,-1,-1):
        if arr[i][0] + i > n:
            continue
        else:
            add_p = max(topDown(i) + arr[n][1],add_p)

    if add_p == 0:
        max_per_person[n] = arr[n][1]
        return max_per_person[n]
    else:
        max_per_person[n] = add_p
        return max_per_person[n]   


N = int(input())
arr = []
for _ in range(N):
    day, price = map(int,input().split())
    arr.append([day,price])

max_per_person = [0 for i in range(N)]

max_p = -10e9
for i in range(len(arr)-1,-1,-1):
    if arr[i][0] + i <= N and max_per_person[i] == 0:   
        max_p = max(max_p,topDown(i))

if max_p == -10e9:
    print(0)
else:
    print(max_p)