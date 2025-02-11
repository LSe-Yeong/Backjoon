N =int(input())

my_map =[]
for _ in range(N):
    my_map.append(list(input().split()))
arr=[]
T_spot=[]
for r in range(N):
    for c in range(N):
        if(my_map[r][c]=='T'):
            T_spot.append((r,c))   


def isPoss(my_map,arr):
    for ar in arr:
        r,c = ar
        my_map[r][c]='O'
    for pot in T_spot:
        row,col = pot
        for r in range(row-1,-1,-1):
            if(my_map[r][col]=='O'):
                break
            if(my_map[r][col]=='S'):
                return False
        for r in range(row+1,N):
            if(my_map[r][col]=='O'):
                break
            if(my_map[r][col]=='S'):
                return False
        for c in range(col-1,-1,-1):
            if(my_map[row][c]=='O'):
                break
            if(my_map[row][c]=='S'):
                return False
            
        for c in range(col+1,N):
            if(my_map[row][c]=='O'):
                break
            if(my_map[row][c]=='S'):
                return False
    return True
                 
result=False
def backT(i):
    global result
    if(i==3):
        if(isPoss(my_map,arr)):
            result=True
        for ar in arr:
            r,c = ar
            my_map[r][c]='X'
        
    else:
        for r in range(N):
            for c in range(N):
                if(my_map[r][c]=='X' and (r,c) not in arr):
                    arr.append((r,c))
                    backT(i+1)
                    arr.pop()

backT(0)
if(result):
    print("YES")
else:
    print("NO")


