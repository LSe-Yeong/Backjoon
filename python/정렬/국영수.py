N = int(input())
peoples=[]

for _ in range(N):
    name,kor,eng,mat = input().split()
    kor =int(kor)
    eng = int(eng)
    mat = int(mat)
    peoples.append((name,kor,eng,mat))

peoples.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for people in peoples:
    print(people[0])
    