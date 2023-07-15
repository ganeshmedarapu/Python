def lastIndexBetter(arr,num,si):
    l=len(arr)
    if num not in arr:
        return -1
    if num==arr[si]:
        return si
    return lastIndexBetter(arr,num,si-1)
arr=[2,5,2,8,5,8]
num=int(input('Enter num: '))
print(lastIndexBetter(arr,num,len(arr)-1))