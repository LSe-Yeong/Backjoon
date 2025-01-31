def isPossible(my_const):
    for f in my_const:
        x,y,a = f
        if(a==0):
            #가능하면 다음꺼, 불가능이면 return False
            if y==0 or (x,y,1) in my_const or (x-1,y,1) in my_const or (x,y-1,0) in my_const:
                continue
            else:
                return False
            
        else:
            if (x,y-1,0) in my_const or (x+1,y-1,0) in my_const or ((x-1,y,1) in my_const and (x+1,y,1) in my_const):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    my_const=[]
    for value in build_frame:
        x,y,a,b = value
        
        if(b==1):
            my_const.append((x,y,a))
            is_poss = isPossible(my_const)
            if(not is_poss):
                my_const.remove((x,y,a))
        else:
            my_const.remove((x,y,a))
            is_poss = isPossible(my_const)
            if(not is_poss):
                my_const.append((x,y,a))
    
    answer = sorted(my_const)
    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
