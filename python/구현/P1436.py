N=int(input())

count=1

for i in range(1,100000000):
    if "666" in str(i):
        count+=1
    if(count==N+1):
        print(i)
        break
           