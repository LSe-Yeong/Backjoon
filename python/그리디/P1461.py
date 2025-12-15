N, M = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
m_arr = []
p_arr = []
results = []

for v in arr:
    if v < 0:
        m_arr.append(v)
    else:
        p_arr.append(v)

if len(m_arr) > 0:
    result = abs(m_arr[0])
    for i in range(M,len(m_arr),M):
        result = result + (abs(m_arr[i] * 2))

    for i in range(len(p_arr)-1,-1,-M):
        result += abs(p_arr[i] * 2)
    results.append(result)

if len(p_arr) > 0:
    result = abs(p_arr[-1])
    for i in range(len(p_arr)-M-1,-1,-M):
        result = result + (abs(p_arr[i] * 2))

    for i in range(0,len(m_arr),M):
        result += abs(m_arr[i] * 2)
    results.append(result)

print(min(results))
