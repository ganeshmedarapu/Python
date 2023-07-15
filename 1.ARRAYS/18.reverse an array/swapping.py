def revArr(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr=[2,5,8,6]
revArr(arr,0,3)
print(arr)




