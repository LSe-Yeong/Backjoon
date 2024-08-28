N=int(input())

dx=[0,-1,0,1]
dy=[1,0,-1,0]
dir=['R','U','L','D']

inst=list(input().split())
x,y=1,1
print(inst)
for i in inst:
    for j in range(0,len(dir)):
        if dir[j]==i:
            nx=x+dx[j] 
            ny=y+dy[j]
    if(nx<1 or nx>N or ny<1 or ny>N):
        continue
    x,y=nx,ny       
print(x,y)         
