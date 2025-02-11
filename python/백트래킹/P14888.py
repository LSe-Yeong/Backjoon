N = int(input())
array = list(map(int,input().split()))
oper_num = list(map(int,input().split()))
length = len(array)

min_value=10e9
max_value=-10e9

def backT(depth,v):
    global max_value,min_value
    if(depth==length):
        max_value=max(max_value,v)
        min_value=min(min_value,v)
    else:
        if(oper_num[0]>0):
            oper_num[0]-=1
            backT(depth+1,v+array[depth])
            oper_num[0]+=1
        if(oper_num[1]>0):
            oper_num[1]-=1
            backT(depth+1,v-array[depth])
            oper_num[1]+=1
        if(oper_num[2]>0):
            oper_num[2]-=1
            backT(depth+1,v*array[depth])
            oper_num[2]+=1
        if(oper_num[3]>0):
            oper_num[3]-=1
            backT(depth+1,int(v/array[depth]))
            oper_num[3]+=1        
            
backT(1,array[0])
print(max_value)
print(min_value)
