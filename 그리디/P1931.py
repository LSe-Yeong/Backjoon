N=int(input())

sch=[]
count=0
end=0

for i in range(N):
    sch.append(list(map(int,input().split())))

sch.sort(key=lambda x: (x[1], x[0]))

for i in range(len(sch)):
    if(sch[i][0]>=end):
        count=count+1
        end=sch[i][1]
            
print(count)    