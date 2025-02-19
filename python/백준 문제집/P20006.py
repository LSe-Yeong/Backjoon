def isPoss(r,l):
    if(r["level"]-10<= l <=r["level"]+10 and len(r["p"])<M):
        return True
    else:
        return False

def enter_room(l,n):
    if(len(rooms)==0):
        rooms.append({"p":[(n,l)],"level":l})
        return
     
    for room in rooms:
        if(isPoss(room,l)):
            room["p"].append((n,l))
            return
    
    rooms.append({"p":[(n,l)],"level":l})
    return    

def make_result():
    for room in rooms:
        room["p"].sort(key=lambda x:x[0])
        
        if(len(room["p"])==M):
            print("Started!")
        else:
            print("Waiting!")
            
        for level,name in room["p"]:
                print(name,end=" ")
                print(level)
    return

import sys
P, M = map(int,sys.stdin.readline().split())
rooms=[]

for _ in range(P):
    l, name = sys.stdin.readline().split()
    l = int(l)
    enter_room(l,name)

make_result()