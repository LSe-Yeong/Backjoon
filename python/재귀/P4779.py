
def slice_str(left,right):
    if(right==left or right==left+1):
        return
    midLeft = int(left + ((right-left)//3))
    midright = int(right - ((right-left)//3))
    for i in range(midLeft+1,midright):
        str_list[i]=" "
    slice_str(left,midLeft)
    slice_str(midright,right) 
    return

while True:
    try:
        N = int(input())
        str_list = list("-" * 3**N)

        left=0
        right=3**N-1

        slice_str(left,right)

        print(''.join(str_list))
    except:
        break



