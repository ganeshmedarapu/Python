def firstIndex(arr,num):
    l=len(arr)
    if num not in arr:      # we can also use if l==0:
        return -1
    if num==arr[0]:
        return 0
    return 1+firstIndex(arr[1:],num)
arr=[2,5,2,8,5,8]
num=int(input('Enter num: '))
print(firstIndex(arr,num))











'''L = [1, 2, 3, 4, 5, 6, 7, 11, 13]

def index(L, v):
    if len(L) == 0:
            return -1000000
    elif L[0] == v:
        return 0
    else:
        return 1 + index(L[1:], v)

print index(L, 7)
print index(L, 13)
print index(L, 100)'''

