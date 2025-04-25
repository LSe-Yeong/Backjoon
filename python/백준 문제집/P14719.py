row,col = map(int,input().split())
blocks = list(map(int,input().split()))

res=0
for i in range(1,col-1):
    left_m = max(blocks[0:i])
    right_m = max(blocks[i+1:])
    water = min(left_m,right_m) - blocks[i]
    if(water>0):
        res+=water

print(res)