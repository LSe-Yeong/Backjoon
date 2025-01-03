import heapq

def polling(array):
    N = len(array)
    if(N==1):
        return array
    new_array=[[0 for _ in range(N//2)] for i in range(N//2)]
    queue=[]
    r_idx=0
    c_idx=0
    for r in range(0,N,2):
        for c in range(0,N,2):
            for row in range(r,r+2):
                for col in range(c,c+2):
                    heapq.heappush(queue,-array[row][col])
            heapq.heappop(queue)
            new_array[r_idx][c_idx]=-heapq.heappop(queue)
            c_idx+=1    
        r_idx+=1
        c_idx=0
    result = polling(new_array)
    return result
    
    
N = int(input())
my_list = []
for _ in range(N):
    my_list.append(list(map(int,input().split()))) 

result = polling(my_list)
print(result)
    


