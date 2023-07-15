def check(arr,num):
    if num not in arr:
        return False
    return arr[0]==num or check(arr[1:],num)
arr=[1,2,3]
num=int(input('Enter num:'))
s=check(arr,num)
print(s)