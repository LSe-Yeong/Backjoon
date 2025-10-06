import sys

def check(students):
    for r,c in students:
        for i in range(r-1,-1,-1):
            if my_map[i][c] == 'O':
                break
            elif my_map[i][c] == 'T':
                return False
        for i in range(r+1,N):
            if my_map[i][c] == 'O':
                break
            elif my_map[i][c] == 'T':
                return False
        for i in range(c-1,-1,-1):
            if my_map[r][i] == 'O':
                break
            elif my_map[r][i] == 'T':
                return False
        for i in range(c+1,N):
            if my_map[r][i] == 'O':
                break
            elif my_map[r][i] == 'T':
                return False
    return True

def backT(v):
    if len(objects) == 3:
        for r,c in objects:
            my_map[r][c] = 'O'
        if(check(students)):
            print("YES")
            sys.exit()
        for r,c in objects:
            my_map[r][c] = 'X'
        return 
    for i in range(v,len(X_lists)):
        objects.append((X_lists[i]))
        backT(i+1)
        objects.pop()

N = int(input())
my_map = []
students = []
X_lists = []
objects = []
result = []
for _ in range(N):
    my_map.append(list(input().split()))

for r in range(N):
    for c in range(N):
        if my_map[r][c] == 'S':
            students.append((r,c))
        elif my_map[r][c] == 'X':
            X_lists.append((r,c))
backT(0)
print("NO")