# 0010011010
# 1011100101

def toggle(i,N,status):
    if i == 0:
        for j in range(0,2):
            if status[j]=='0':
                status[j] = '1'
            else:
                status[j] = '0'
    elif i == N-1:
        for j in range(i-1,N):
            if status[j]=='0':
                status[j] = '1'
            else:
                status[j] = '0'
    else:
        for j in range(i-1,i+2):
            if status[j]=='0':
                status[j] = '1'
            else:
                status[j] = '0'

N = int(input())
status = list(input())
target = list(input())

sample_status = []
for ele in status:
    sample_status.append(ele)

result = -1
count = 0
for i in range(1,N):
    if status[i-1] != target[i-1]:
        count+=1
        toggle(i,N,status)

if status[-1] == target[-1]:
    result = count 

count = 1
toggle(0,N,sample_status)
for i in range(1,N):
    if sample_status[i-1] != target[i-1]:
        count+=1
        toggle(i,N,sample_status)

if sample_status[-1] == target[-1] and (count < result and result != -1):
    result = count 

print(result)





