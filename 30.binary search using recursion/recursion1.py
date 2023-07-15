def binarySearch(arr,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if arr[mid]==x:
        return mid
    elif arr[mid]>x:
        return binarySearch(arr,x,si,mid-1)
    else:
        return binarySearch(arr,x,mid+1,ei)
print(binarySearch([1,2,3,6,7,9,13,15],9,0,7))