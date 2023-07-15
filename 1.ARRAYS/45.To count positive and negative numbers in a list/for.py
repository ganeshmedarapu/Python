arr=list(map(int,input().split()))
p_count = 0
n_count = 0
for i in arr:
    if i>=0:
        p_count+=1
    else:
        n_count+=1
print(p_count)
print(n_count)