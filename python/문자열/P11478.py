word=input()
sub_list=[]


for length in range(1,len(word)+1):
    for i in range(len(word)-length+1):
        sub_list.append(word[i:i+length])

print(len(set(sub_list)))
        