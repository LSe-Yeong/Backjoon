T = int(input())
for _ in range(T):
    alphas = "abcdefghijklmnopqrstuvwxyz" 
    st = input()
    K = int(input())
    INF = 10e9
    max_len = -INF
    min_len = INF
    for c in alphas:
        count=1
        left= right = st.find(c)
        if(st.count(c)<K):
            continue
        if(K==1):
            break

        while right<len(st)-1:
            right+=1
            if(st[right]==c):
                count+=1
            if(count==K):
                length = right-left+1
                max_len = max(max_len,length)
                min_len = min(min_len,length)
                left+=1
                count-=1
                while st[left]!=c:
                    left+=1
    if(min_len==INF):
        if(K==1):
            print(1,end=" ")
            print(1,end=" ")
        else:
            print(-1,end=" ")
    else:
        print(min_len, end=" ")
        print(max_len,end=" ")
        



        
