#완전탐색
# from itertools import permutations

# N = int(input())
# array = list(map(int,input().split()))
# oper = list(map(int,input().split()))
# oper_Type = ["+","-","*","/"]
# oper_array= []
# for i in range(len(oper)):
#     for j in range(oper[i]):
#         oper_array.append(oper_Type[i])

# oper_iter = list(permutations(oper_array))

# results=[]
# for ops in oper_iter:
#     result=array[0]
#     for i in range(len(ops)):
#         op = ops[i]
#         if(op=='+'):
#             result+=array[i+1]
#         elif(op=="-"):
#             result-=array[i+1]
#         elif(op=="*"):
#             result*=array[i+1]
#         else:
#             if(result<0):
#                 result=(-result)
#                 result//=array[i+1]
#                 result=(-result)
#             else:
#                 result//=array[i+1]
#     results.append(result)

# print(max(results))
# print(min(results))            

##DFS

def backT(value,idx):
    if idx == N:
        result.append(value)
    if opers[0] != 0:
        opers[0] -= 1
        backT(value+arr[idx],idx+1)
        opers[0] += 1
    if opers[1] != 0:
        opers[1] -= 1
        backT(value-arr[idx],idx+1)
        opers[1] += 1
    if opers[2] != 0:
        opers[2] -= 1
        backT(value*arr[idx],idx+1)
        opers[2] += 1
    if opers[3] != 0:
        opers[3] -= 1
        div_v = 0
        if value < 0:
            div_v = -((-value) // arr[idx])
        else:
            div_v = value // arr[idx]
        backT(div_v,idx+1)
        opers[3] += 1


N = int(input())
arr = list(map(int,input().split()))
opers = list(map(int,input().split()))
result = []

backT(arr[0],1)

print(max(result))
print(min(result))



