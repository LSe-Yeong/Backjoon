N = int(input())

Q_map = [0 for _ in range(N)]

def check(row,col):
    for r in range(row):
        if col==Q_map[r] or row-r == abs(col-Q_map[r]):
            return False
    return True
    
count=0
def backT(c):
    global count
    if(c==N):
        count=count+1
        return
    else:
        for i in range(N):
            if(check(c,i)):
                Q_map[c]=i
                backT(c+1)

backT(0)
print(count)