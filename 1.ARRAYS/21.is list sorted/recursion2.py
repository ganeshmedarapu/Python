def isSortedBetter(arr,si):
    l=len(arr)
    if si==l-1 or si==l:
        return True
    if arr[si]>arr[si+1]:
        return False
    return isSortedBetter(arr,si+1)
arr=[5,8,3,4]
print(isSortedBetter(arr,0))