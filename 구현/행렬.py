N,M1=map(int,input().split())
mat1=[]
mat2=[]
for _ in range(N):
    mat1.append(list(map(int,input().split())))
M2,K=map(int,input().split())
for _ in range(M2):
    mat2.append(list(map(int,input().split())))
    
result=[[0 for i in range(K)] for _ in range(N)]    
    
for row in range(N):
    for col in range(K):
        sum=0
        for i in range(M1):
            sum=sum+mat1[row][i]*mat2[i][col]
        result[row][col]=sum

for i in range(N):
    for j in range(K):
        print(result[i][j], end=" ")
    print()