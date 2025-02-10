N, M = map(int,input().split())

s6=[]
s1=[]

for _ in range(M):
    v1,v2 = map(int,input().split())
    s6.append(v1)
    s1.append(v2)

s1.sort()
s6.sort()

s1_price = s1[0]
s6_price = s6[0]

sum=0
while(N>0):
    if(N>=6):
        if(s6_price<s1_price*6):
            sum+=s6_price
        else:
            sum+=s1_price*6
        N-=6
    else:
        if(s6_price<s1_price*N):
            sum+=s6_price
            N-=6
        else:
            sum+=s1_price*N
            N-=N
        
print(sum)