arr=[5,-8,-58,64,26]
n=len(arr)
max=arr[0]
for i in range(n):
    if arr[i]>max:
        max=arr[i]
print(max)