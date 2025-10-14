def backT(N,buffer,solve):
    if len(buffer) == N-1:
        num_list = [1]
        answer = "1"

        for i in range(2,len(buffer)+2):
            if buffer[i-2] == ' ':
                answer += (' ' + str(i)) 
                num_list[-1] = int(str(num_list[-1])+str(i))
            else:
                answer += (buffer[i-2]+str(i))
                num_list.append(i)

        idx = 0
        result = num_list[0]
        for i in range(len(buffer)):
            if buffer[i] == ' ':
                continue
            elif buffer[i] == '+':
                result += num_list[idx+1]
                idx+=1
            else:
                result -= num_list[idx+1]
                idx+=1
        
        if result == 0:
            solve.append(answer)

        return
    
    for ch in ["+","-"," "]:
        buffer.append(ch)
        backT(N,buffer,solve)
        buffer.pop()

T = int(input())

for _ in range(T):
    N = int(input())
    buffer = []
    solve = []
    backT(N,buffer,solve)
    solve.sort()
    for st in solve:
        print(st)
    print()
