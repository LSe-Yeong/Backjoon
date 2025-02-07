
def solu():
    N, M = map(int,(input().split()))

    count=0
    while(M>0):
        if(N==M):
            count+=1
            break
        else:
            if(M%10==1):
                if(M!=1):
                    M=M//10
                else:
                    print(-1)
                    return
            else:
                if(M<N or M%2==1):
                    print(-1)
                    return
                elif(M%2==0):
                    M=M//2
            count+=1
    print(count)    

solu()