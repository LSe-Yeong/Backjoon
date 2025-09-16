import heapq

# def solution(food_times, k):
#     q=[]
#     if sum(food_times) <= k:
#         return -1
    
#     for i in range(len(food_times)):
#         heapq.heappush(q,(food_times[i],i+1))
  
#     total_dif = 0
#     while(q[0][0]-total_dif) * len(q) <= k and k!=0:
#         length = len(q)
#         value = heapq.heappop(q)[0]
#         k -= length * (value - total_dif)
#         total_dif += (value-total_dif)
    
#     q.sort(key=lambda x:x[1])
#     answer = (q[k%len(q)][1])
#     return answer

import heapq

def solution(food_times, k):
    q=[]
    is_left = [True for i in range(len(food_times))]
    temp = 0
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    while q:
        min_v,idx = q[0]
        min_v -= temp
        if (min_v * (len(q))) > k:
            q.sort(key=lambda x : x[1])
            return q[k%len(q)][1]
        else:
            is_left[idx-1] = False
            k-=((len(q))*min_v)
            temp += min_v
            heapq.heappop(q)
    return -1

print(solution([3,1,2],6))      