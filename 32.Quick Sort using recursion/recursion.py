def partition(arr,si,ei):
    pivot=arr[si]
    c=0
    for i in range(si,ei+1):
        if arr[i]<pivot:
            c=c+1
    arr[si],arr[si+c]=arr[si+c],arr[si]
    pivot_index=si+c
    i=si
    j=ei
    while i<j:
        if arr[i]<pivot:
            i=i+1
        elif arr[j]>pivot:
            j=j-1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
            j=j-1
    return pivot_index
    
def quick_sort(arr,si,ei):
    if si>=ei:
        return
    pivot_index=partition(arr,si,ei)
    quick_sort(arr,si,pivot_index-1)
    quick_sort(arr,pivot_index+1,ei)

arr=[2,4,1,0,6,3,8,5,7]

#printing partition
partition(arr,0,len(arr)-1)
print(arr)

#printing quick_sort
quick_sort(arr,0,len(arr)-1)
print(arr)

