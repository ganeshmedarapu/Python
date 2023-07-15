arr=list(map(int,input().split()))
p_count = 0
n_count = 0
i = 0
while i<len(arr):
    if arr[i]>=0:
        p_count+=1
    else:
        n_count+=1
    i+=1
print(p_count)
print(n_count)