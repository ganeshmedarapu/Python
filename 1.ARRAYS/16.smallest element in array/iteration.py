arr=[5,2,-9,58]
n=len(arr)
min=arr[0]
for i in range(n):
    if arr[i]<min:
        min=arr[i]
print(min)