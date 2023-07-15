from functools import reduce
arr = list(map(int,input().split()))
largest_ele = reduce(max,arr)
print(largest_ele)