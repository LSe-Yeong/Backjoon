N=int(input())
count=0

while True:
    if(N%5==0):
        count+=(N//5)
        print(count)
        break        
    else:
        N-=3
        count+=1
    if(N<=-1):
        print(-1)
        break