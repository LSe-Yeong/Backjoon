N = int(input())

array=[]

for _ in range(N):
    array.append(list(map(int,input().split())))

for r in range(1,N):
    for c in range(len(array[r])):
        if c == 0:
            array[r][c] = array[r][c] + array[r-1][c]
        elif c== len(array[r])-1:
            array[r][c] = array[r][c] + array[r-1][c-1]
        else:
            array[r][c] = array[r][c] + max(array[r-1][c],array[r-1][c-1])

print(max(array[-1]))
        