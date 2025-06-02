N = int(input())
isUsed = set()
result=[]
for _ in range(N):
    isOver=False
    option_location = 0
    word_set = input().split()
    for i in range(len(word_set)):
        if not word_set[i][0] in isUsed:
            isUsed.add(word_set[i][0].lower())
            isUsed.add(word_set[i][0].upper())
            option_location = [i,0]
            isOver=True
            break
    if not isOver:
        for w in range(len(word_set)):
            for i in range(1,len(word_set[w])):
                if not word_set[w][i] in isUsed:
                    isUsed.add(word_set[w][i].lower())
                    isUsed.add(word_set[w][i].upper())
                    isOver=True
                    option_location = [w,i]
                    break
            if isOver:
                break
    
    result_word = ""
    if(not isOver):
        for word in word_set:
            result_word+= word+" "
        print(result_word)
    else:
        for i in range(len(word_set)):
            if i == option_location[0]:
                result_word+=(word_set[i][0:option_location[1]]+"["+word_set[i][option_location[1]]+"]"+word_set[i][option_location[1]+1:])
            else:
                result_word+=word_set[i]
            result_word+=" "
        
        print(result_word)
