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

N = int(input())
array = list(map(int,input().split()))
oper = list(map(int,input().split()))
oper_Type = ["+","-","*","/"]
oper_array= []
for i in range(len(oper)):
    for j in range(oper[i]):
        oper_array.append(oper_Type[i])

