arr=list(map(int,input().split()))
p = [i for i in arr if i>=0]
p_count = len(p)
n_count = len(arr) - p_count
print(p_count)
print(n_count)