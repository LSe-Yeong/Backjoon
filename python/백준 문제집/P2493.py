N = int(input())
tops = list(map(int,input().split()))
stack = [[tops[-1],len(tops)-1]]
result = [0 for _ in range(N)]

for i in range(len(tops)-2,-1,-1):
    if tops[i] < stack[-1][0]:
        stack.append([tops[i],i])
    else:
        while len(stack)!=0 and stack[-1][0]<tops[i]:
            h,idx = stack.pop()
            result[idx] = i+1
        stack.append([tops[i],i])

for v in result:
    print(v,end=" ")

