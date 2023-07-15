def firstIndex(arr,num):
    l=len(arr)
    if num not in arr:     # we can also use if l==0:
        return -1
    if num==arr[0]:
        return 0
    k=firstIndex(arr[1:],num)    # k returns the position(index) of num
    if k==-1:
        return -1
    else:
        return k+1
arr=[2,5,2,8,5,8]
num=int(input('Enter num: '))
print(firstIndex(arr,num))