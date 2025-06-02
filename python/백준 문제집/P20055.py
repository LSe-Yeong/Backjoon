from collections import deque

N,K = map(int,input().split())
array = list(map(int,input().split()))
belts = deque()
for i in range(1,len(array)+1):
    belts.append({"id":i,"isRobot":False,"durability":array[i-1],"isCheck":False})

def rotate_belt(belts):
    belts.appendleft(belts.pop())
    if(belts[(len(belts)//2)-1]["isRobot"]):
        belts[(len(belts)//2)-1]["isRobot"] = False

def move_robot(belts):
    for i in range((len(belts)//2)-2,-1,-1):
        if(belts[i]["isRobot"] and not belts[i+1]["isRobot"] and belts[i+1]["durability"]>=1):
            if(i==(len(belts)//2)-2):
                belts[i]["isRobot"] = False
                belts[i+1]["durability"] -= 1
            else: 
                belts[i]["isRobot"] = False
                belts[i+1]["isRobot"] =True
                belts[i+1]["durability"] -= 1

def up_robot(belts):
    if(belts[0]["durability"]!=0):
        belts[0]["isRobot"] = True
        belts[0]["durability"] -= 1

def isCheck(belts):
    count_zero = 0
    for belt in belts:
        if(belt["durability"]==0):
            count_zero+=1
    if(count_zero>=K):
        return True
    else:
        return False

count = 1
while True:
    rotate_belt(belts)
    move_robot(belts)
    up_robot(belts)
    if(isCheck(belts)):
        break
    count+=1

print(count)

