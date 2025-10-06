from bisect import bisect_left,bisect_right

def check_count(q,arr):
    left_q = q.replace('?','a')
    right_q = q.replace('?','z')
    left_idx = bisect_left(arr,left_q)
    right_idx = bisect_right(arr,right_q)
    return right_idx - left_idx

def solution(words, queries):
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    result = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    
    for i in range(1,10001):
        array[i].sort()
        reversed_array[i].sort()

    for i in range(len(queries)):
        query = queries[i]
        if query[0]=='?':
            query = query[::-1]
            result.append(check_count(query,reversed_array[len(query)]))
        else:
            result.append(check_count(query,array[len(query)]))

    return result

print(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"]
))
