import itertools

N,M=map(int,input().split())

city=[]
chicken=[]
result=[]

for _ in range(N):
    city.append(list(map(int,input().split())))

for row in range(N):
    for col in range(N):
        if(city[row][col]==2):  
            chicken.append({"row":row,"col":col})

chicken_combi=list(itertools.combinations(chicken,M))

for ch in chicken_combi:
    sum=0
    for row in range(N):
        for col in range(N):
            if(city[row][col]==1):
                distance=[]
                for i in range(len(ch)):
                    distance.append(abs(ch[i]["row"]-row)+abs(ch[i]["col"]-col))
                sum+=min(distance)
    result.append(sum)               
            
print(min(result))
