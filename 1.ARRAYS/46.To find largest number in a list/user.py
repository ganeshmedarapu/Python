list = []
numbers = int(input('Enter number of elements:'))
for i in range(1,numbers+1):
    ele = int(input('Enter a number:'))
    list.append(ele)
print(max(list))
