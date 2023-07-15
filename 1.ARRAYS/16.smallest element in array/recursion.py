def findMin(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n-1], findMin(arr, n - 1))
 

arr = [1, 4, 45, -60, -50, 10, 2]
n = len(arr)
print(findMin(arr, n))