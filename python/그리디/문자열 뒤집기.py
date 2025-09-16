# myStr = list(map(int,input()))

# count = [0,0]

# count[myStr[0]]+=1

# for i in range(len(myStr)-1):
#     if(myStr[i]!=myStr[i+1]):
#         count[myStr[i+1]]+=1

# print(min(count))
            
arr = input()

ps = ["0","1"]
isConti = False
result = []

for p in ps:
    idx = 0
    count=0
    while idx<len(arr):
        if arr[idx] != p:
            count+=1
            while idx<len(arr) and arr[idx]!=p:
                idx+=1
        idx+=1
    result.append(count)

print(min(result))

