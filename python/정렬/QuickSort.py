def quickSort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = arr[len(arr)//2]
    arr_less,arr_equal,arr_more = [],[],[]
    for n in arr:
        if n<pivot:
            arr_less.append(n)
        elif n>pivot:
            arr_more.append(n)
        else:
            arr_equal.append(n)
    return quickSort(arr_less) + arr_equal + quickSort(arr_more)

arr=[1,7,3,5,9,10,2,4,8]

arr=quickSort(arr)

print(arr)