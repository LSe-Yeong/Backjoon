def solution(N, stages):
    fail_rate = [[0,i+1] for i in range(N)]
    stages.sort()
    idx = 0
    while idx < len(stages):
        count = 1
        value = stages[idx]
        while idx!=len(stages)-1 and stages[idx]==stages[idx+1]:
            idx+=1
            count+=1
        if value != N+1:
            fail_rate[value-1][0] = count / (count+len(stages)-idx-1)
        idx+=1
    
    fail_rate.sort(key = lambda x: -x[0])
    answer = []
    for i in range(len(fail_rate)):
        answer.append(fail_rate[i][1])
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))