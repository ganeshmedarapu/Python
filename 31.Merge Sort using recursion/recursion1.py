def merge(arr1,arr2,arr):
    i=0
    j=0
    k=0   #index of arr
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i=i+1
            k=k+1
        else:
            arr[k]=arr2[j]
            j=j+1
            k=k+1
    while i<len(arr1):
        arr[k]=arr1[i]
        i=i+1
        k=k+1
    while j<len(arr2):
        arr[k]=arr2[j]
        j=j+1
        k=k+1

def merge_sort(arr):
    if len(arr)==0 or len(arr)==1:
        return
    mid=len(arr)//2
    arr1=arr[0:mid]
    arr2=arr[mid:]
    
    merge_sort(arr1)
    merge_sort(arr2)

    merge(arr1,arr2,arr)
arr=[10,3,2,9,4,6,1]
merge_sort(arr)
print(arr)