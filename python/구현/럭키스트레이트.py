N = input()

# leftSum=0
# rightSum=0

# for i in range(len(N)//2):
#     leftSum+=int(N[i])
# for i in range(len(N)//2,len(N)):
#     rightSum+=int(N[i])

# if(leftSum==rightSum):
#     print("LUCKY")
# else:
#     print("READY")

sum_1 = 0
for i in range(len(N)//2):
    sum_1 += int(N[i])
sum_2 = 0
for i in range(len(N)//2,len(N)):
    sum_2 += int(N[i])

if(sum_1==sum_2):
    print("LUCKY")
else:
    print("READY")
