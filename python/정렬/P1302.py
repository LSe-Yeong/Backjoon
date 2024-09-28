book_list=[]

N=int(input())

for i in range(N):
    book=input()
    isExist=False
    for j in range(len(book_list)):
        if(book_list[j]["name"]==book):
            isExist=True
            book_list[j]["count"]+=1
            break
    if(not isExist):
        book_list.append({"name":book,"count":1})

book_list.sort(key= lambda x: (-x["count"], x["name"]))

print(book_list[0]["name"])