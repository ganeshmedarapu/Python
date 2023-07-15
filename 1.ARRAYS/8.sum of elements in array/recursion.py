def getSum(arr,n):
    if n==0:
        return 0
    return arr[n-len(arr)]+getSum(arr,n-1)
arr=[11,22,33]
print(getSum(arr,len(arr)))