def findMax(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1],findMax(arr,n-1))
arr=[1,5,82,-5,-80]
n=len(arr)
print(findMax(arr,n))