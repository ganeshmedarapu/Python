def lastIndex(arr,num):
    l=len(arr)
    if num not in arr:     # we can also use if l==0:
        return -1
    output=lastIndex(arr[1:],num)       # output returns the position(index) of num
    if output !=-1:
        return output+1
    else:
        if arr[0]==num:
            return 0
        else:
            return -1
arr=[2,5,2,8,5,8]
num=int(input('Enter num: '))
print(lastIndex(arr,num))

