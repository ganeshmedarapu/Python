def firstIndexBetter(arr,num,si):
    l=len(arr)
    if num not in arr:
        return -1
    if num==arr[si]:
        return si
    return firstIndexBetter(arr,num,si+1)
arr=[2,5,2,8,5]
num=int(input('Enter num: '))
print(firstIndexBetter(arr,num,0))