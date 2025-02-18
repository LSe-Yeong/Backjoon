def similar_str(dic1,dic2):
    if(dic1==dic2):
        return True
    if(not -2<abs(sum(dic1.values())-sum(dic2.values()))<2):
        return False
    
    diff=dict()
    
    for key in dic2.keys():
        if key in dic1:
            diff[key]=dic2[key]-dic1[key]
        else:
            diff[key]=dic2[key]
    
    for key in dic1.keys():
        if key not in dic2:
            diff[key]=-dic1[key]
    
    count_n_zero=0
    for key in diff.keys():
        if diff[key]!=0:
            if(diff[key]<-1 or diff[key]>1):
                return False
            count_n_zero+=1
    
    if(count_n_zero>=3):
        return False
    elif(count_n_zero==2 and sum(diff.values())!=0):
        return False
    else:
        return True

def make_dic(str):
    dic = dict()
    for ch in str:
        if ch in dic:
            dic[ch]+=1
        else:
            dic[ch]=1
            
    return dic        

import sys
N = int(sys.stdin.readline())
target=make_dic(sys.stdin.readline())

result=0
for _ in range(1,N):
    word = make_dic(sys.stdin.readline())
    if(similar_str(target,word)):
        result+=1
        
print(result)
    
    