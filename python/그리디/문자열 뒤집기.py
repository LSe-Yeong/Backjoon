myStr = list(map(int,input()))

count = [0,0]

count[myStr[0]]+=1

for i in range(len(myStr)-1):
    if(myStr[i]!=myStr[i+1]):
        count[myStr[i+1]]+=1

print(min(count))
            