def isOk(st):
    stack = []
    for ch in st:
        if ch == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True

def changeU(u):
    newU = ''
    result = ''
    for i in range(1,len(u)-1):
        newU += u[i]
    for i in range(len(newU)):
        if newU[i] == '(':
            result+=')'
        else:
            result+='('
    return result
    

def process(answer,p):
    if p=='':
        return ''
    u=''
    v=''
    left_c = 0
    right_c = 0
    for i in range(len(p)):
        if p[i]=='(':
            left_c+=1
        else:
            right_c+=1
        u+=p[i]
        if left_c==right_c and left_c !=0:
            if i == len(p)-1:
                v = ''
            else:
                v = p[i+1:]
            break
    if isOk(u):
        return u + process(answer,v)
    else:
        newV = process(answer,v)
        newU = changeU(u)
        return '('+newV+')'+newU
        
def solution(p):
    answer = ''
    answer = process(answer,p)
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

