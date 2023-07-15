def revArr(arr,start,end):
    if start>=end:
        return arr
    arr[start],arr[end]=arr[end],arr[start]
    revArr(arr,start+1,end-1)
arr=[2,5,4,6,12,64]
revArr(arr,0,5)
print(arr)

    



