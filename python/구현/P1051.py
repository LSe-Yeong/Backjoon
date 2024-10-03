

N,M=map(int,input().split())
array=[]

for _ in range(N):
    array.append(list(map(int,input())))

max_size=1
for size in range(2,min(N,M)+1):
    for r in range(N-size+1):
        for c in range(M-size+1):
           if(array[r][c]==array[r+size-1][c]==array[r][c+size-1]==array[r+size-1][c+size-1]):
               max_size=size

print(max_size ** 2)

    