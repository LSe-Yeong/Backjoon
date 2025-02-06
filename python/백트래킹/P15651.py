N,M = map(int,input().split())
array = []

def backT():
    if(len(array)==M):
        for v in array:
            print(v,end=" ")
        print()
    else:
        for i in range(1,N+1):
            array.append(i)
            backT()
            array.pop()

backT()