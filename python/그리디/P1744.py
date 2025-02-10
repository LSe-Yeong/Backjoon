N = int(input())
nagative=[]
positive=[]
for _ in range(N):
    num = int(input())
    if(num <= 0):
        nagative.append(num)
    else:
        positive.append(num)
        
nagative.sort()
positive.sort(reverse=True)

sum=0

for i in range(0,len(positive),2):
    if(i+1 == len(positive)):
        sum = sum + positive[i]
    else:
        m_sum = positive[i] + positive[i+1]
        m_mul = positive[i] * positive[i+1]
        if(m_mul>m_sum):
            sum+=m_mul
        else:
            sum+=m_sum
            
for i in range(0,len(nagative),2):
    if(i+1==len(nagative)):
        sum+=nagative[i]
    else:
        m_sum = nagative[i] + nagative[i+1]
        m_mul = nagative[i] * nagative[i+1]
        if(m_mul>m_sum):
            sum+=m_mul
        else:
            sum+=m_sum

print(sum)