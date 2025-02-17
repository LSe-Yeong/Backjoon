import sys

def add(S,x):
    S.add(x)
    
def remove(S,x):
    if x in S:
        S.discard(x)
    
def check(S,x):
    if x in S:
        print(1)
    else:
        print(0)

def toggle(S,x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def all(S):
    S = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"}
    return S

def empty(S):
    S=set()
    return S

M = int(input())
s = set()
    
for _ in range(M):
    oper = sys.stdin.readline().split()
    if(oper[0]=="all"):
        s = all(s)
    elif(oper[0]=="empty"):
        s = empty(s)
    else:
        op, n = oper
        if(op=="add"):
            add(s,n)
        elif(op=="remove"):
            remove(s,n)
        elif(op=="check"):
            check(s,n)
        elif(op=="toggle"):
            toggle(s,n)

    
   