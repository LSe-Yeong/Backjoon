movement=[]

K = int(input())

for i in range(6):
    direction, value = map(int,input().split())
    movement.append({"dir":direction,"value":value})

max_width_idx=0
max_height_idx=0
for idx in range(len(movement)):
    if(movement[idx]["dir"] in [3,4]):
        if(movement[max_height_idx]["value"]<=movement[idx]["value"]):
            max_height_idx=idx
    else:
        if(movement[max_width_idx]["value"]<=movement[idx]["value"]):
            max_width_idx=idx 

small_width=abs(movement[max_height_idx-1]["value"]-movement[(max_height_idx+1)%6]["value"])
small_height=abs(movement[max_width_idx-1]["value"]-movement[(max_width_idx+1)%6]["value"])
small_area=small_width * small_height
big_area=movement[max_height_idx]["value"] * movement[max_width_idx]["value"]
area=big_area-small_area
print(area*K)