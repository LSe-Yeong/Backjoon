N = int(input())
crains = list(map(int,input().split()))
M = int(input())
items = list(map(int,input().split()))

crains.sort(reverse=True)
items.sort(reverse=True)

c_idx = 0
i_idx = 0
time = 0

flag = False
while i_idx < len(items):
    if crains[c_idx] >= items[i_idx]:
        flag = True
        i_idx += 1
        c_idx += 1
    else:
        c_idx += 1
    
    if c_idx == len(crains):
        if not flag:
            time = -1
            break
        time += 1
        c_idx = 0
        flag = False

if c_idx != 0 and time != -1:
    time += 1

print(time)


