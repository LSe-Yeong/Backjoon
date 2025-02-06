N,M = map(int,input().split())
array = []

def backT(va):
    if(len(array)==M):
        for v in array:
            print(v,end=" ")
        print()
    else:
        for i in range(va,N+1):
            array.append(i)
            backT(i)
            array.pop()
            
backT(1)
        