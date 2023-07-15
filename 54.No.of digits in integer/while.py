'''
Approach 1

num = int(input('Enter any number:'))
num1 = str(num)
print(len(num1))'''


# Approach 2
x=int(input("Enter any number:"))
count=0
while x!=0:
    remainder=x%10
    x//=10
    count+=1
print(count)