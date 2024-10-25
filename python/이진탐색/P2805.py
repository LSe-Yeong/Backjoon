N,M = map(int,input().split())
tree=list(map(int,input().split()))

result=[]

left=0
right=1000000000

while left<=right:
    mid=(left+right)//2
    count_of_tree=0
    for value in tree:
        if(value>mid):
            count_of_tree+=(value-mid)
    if(count_of_tree<M):
        right=mid-1
    elif(count_of_tree>=M):
        left=mid+1
        result.append({"count":count_of_tree,"height":mid})
   
max_value=0
for item in result:
    if(item["height"]>max_value):
        max_value=item["height"]

print(max_value)