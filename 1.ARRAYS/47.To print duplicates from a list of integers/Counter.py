from collections import Counter
arr = list(map(int,input().split()))
dic = Counter(arr)
print(dic)
list1 = [key for key in dic if dic[key]>1]
print(list1)