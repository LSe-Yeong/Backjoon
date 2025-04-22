S = input()
T = input()
new_T = T
result = 0

def subT(st):
    global result
    if(st==S):
        result = 1
        return
    elif(len(st)<=len(S)):
        return
    if(st[-1]=='A'):
        subT(st[0:len(st)-1])
    if(st[0]=='B'):
        subT(st[-1:0:-1])

subT(T)
print(result)
