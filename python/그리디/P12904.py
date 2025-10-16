#뒤부터!

st1 = list(input())
st2 = list(input())

result = 0
while True:
    if len(st2) == 0:
        break
    if st1 == st2:
        result = 1
        break
    if st2[-1] == 'A':
        st2.pop()
    else:
        st2.pop()
        st2.reverse()

print(result)



