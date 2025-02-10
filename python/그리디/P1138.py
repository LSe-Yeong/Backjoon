from itertools import permutations

N = int(input())
array = list(map(int,input().split()))

height = [0 for _ in range(N)]
for i in range(N):
    height[i]=i+1
    
people_list = list(permutations(height,N))

for combi in people_list:
    taller=[0 for _ in range(N)]
    for i in range(len(combi)):
        count=0
        for j in range(0,i):
            if(combi[i]<combi[j]):
                count+=1
        taller[combi[i]-1]=count
    if(array==taller):
        for v in combi:
            print(v,end=" ")
        break
        