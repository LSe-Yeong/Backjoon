from itertools import permutations

def solution(n, weaks, dist):
    weak = []
    for v in weaks:
        weak.append(v)
    for v in weaks:
        weak.append(v+n)
    prob = list(permutations(dist,len(dist)))
    answer = len(dist) + 1
    for p in prob:
        for start in range(len(weak)//2):
            count = 1
            posible = weak[start] + p[count-1]
            for idx in range(start,start+len(weak)//2):
                if posible < weak[idx]:
                    count+=1
                    if count > len(dist):
                        break
                    posible = weak[idx] + p[count-1] 
            answer = min(answer,count)

    return answer

print(solution(12,[1,5,6,10],[1,2,3,4]))
print(solution(12,[1,3,4,9,10],[3,5,7])) 
