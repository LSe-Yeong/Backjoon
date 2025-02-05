N, M = map(int, input().split())
ans = []

def backT(l,v):
    if l == M:
        for v in ans:
            print(v,end=" ")
        print()
    else:
        for i in range(v,N+1):
            if i not in ans:
                ans.append(i)
                backT(l+1,ans[l]+1)
                ans.pop()

backT(0,1)