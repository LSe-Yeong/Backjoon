def find_area(gidung,max_l):
    h = gidung[0][1]
    area=0
    for i in range(len(gidung)):
        if(gidung[i][0]==max_l):
            area += gidung[i][1]
            break
        if(gidung[i+1][1]>h):
            area += ((gidung[i+1][0]-gidung[i][0]) * h)  
            h = gidung[i+1][1]
        else:
            area += ((gidung[i+1][0]-gidung[i][0])* h)  
    
    h = gidung[-1][1]
    for i in range(len(gidung)-1,-1,-1):
        if(gidung[i][0]==max_l):
            break
        if(gidung[i-1][1]>h):
            area += ((gidung[i][0]-gidung[i-1][0]) * h)  
            h = gidung[i-1][1]
        else:
            area += ((gidung[i][0]-gidung[i-1][0])* h)  
    
    return area       
        

import sys

N = int(sys.stdin.readline())
gidung = []
max_h=-10e9
max_l=-1
for _ in range(N):
    l,h = map(int,sys.stdin.readline().split())
    gidung.append((l,h))
    max_h = max(max_h,h)
    if(max_h==h):
        max_l = l

gidung.sort()
area = find_area(gidung,max_l)
print(area)

