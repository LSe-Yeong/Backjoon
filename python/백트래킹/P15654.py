N,M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
ans = []

def backT():
    if(len(ans)==M):
        for v in ans:
            print(v,end=" ")
        print()
    else:
        for value in array:
            if value not in ans:
                ans.append(value)
                backT()
                ans.pop()

backT()