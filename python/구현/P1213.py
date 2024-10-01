s=input()
array=[0 for _ in range(26)]
odd_count=0
isvalid=True
result=[0 for _ in range(len(s))]

for i in range(len(s)):
    array[ord(s[i])-ord('A')]+=1

for value in array:
    if(value%2==1):
        odd_count+=1
    if(odd_count==2):
        isvalid=False
        break

i=0

if(isvalid):
    for t in range((len(s) // 2) +1):
        for j in range(len(array)):
            if(array[j]==1):
                result[len(s) // 2] = chr(j+65)
                array[j]-=1
                break
            elif(array[j]>0):
                result[i]=chr(j+65)
                result[len(s)-i-1]=chr(j+65)
                array[j]-=2
                i+=1
                break            
    print(''.join(result))
    
else:
    print("I'm Sorry Hansoo")
    
