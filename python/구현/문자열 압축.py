def slice_str(s,n):
    count=1
    result=""
    for i in range(0,len(s),n):
        if(s[i:i+n]==s[i+n:i+2*n]):
            count+=1
        else:
            if(count!=1):
                result+=(str(count)+s[i:i+n])
            else:
                result+=s[i:i+n]
            count=1

    return len(result)
            
def solution(s):
    if(len(s)==1):
        return 1
    min_value=100000
    for i in range(1,len(s)//2+1):
        value = slice_str(s,i)
        if(value <= min_value):
            min_value = value

    return min_value