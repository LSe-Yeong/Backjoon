spot=input()
col=int(ord(spot[0]))-ord("a")+1
row=int(spot[1])

dRow=[-2,-2,-1,-1,1,1,2,2]
dCol=[1,-1,2,-2,2,-2,1,-1]
count=0

for i in range(0,8):
    nRow=row+dRow[i]
    nCol=col+dCol[i]
    if(nRow<1 or nRow>8 or nCol<1 or nCol>8):
        continue
    count+=1

print(count)