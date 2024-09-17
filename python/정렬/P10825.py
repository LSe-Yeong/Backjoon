N=int(input())
students=[]

for i in range(N):
    name,kor,eng,math=input().split()
    kor=int(kor)
    math=int(math)
    eng=int(eng)
    students.append({"name":name,"kor":kor,"math":math,"eng":eng})

students.sort(key= lambda x: (-x['kor'], x["eng"], -x["math"], x["name"]))

for i in range(N):
    print(students[i]["name"])

