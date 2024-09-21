N=int(input())
distance = list(map(int,input().split()))
city = list(map(int,input().split()))

idx=0
total=0
for i in range(1,len(city)):
    if(city[idx]>=city[i]):
        total+=(city[idx]*sum(distance[idx:i]))
        idx=i
    else:
        if(i==len(city)-1):
            total+=(city[idx]*sum(distance[idx:i]))
            
print(total)
    
        
    