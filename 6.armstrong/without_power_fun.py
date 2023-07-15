from math import remainder


n=int(input('Enter a number: '))
l=len(str(n))
temp=n
sum=0
while temp!=0:
    remainder=temp%10
    sum=sum+(remainder**l)
    temp//=10
if n==sum:
    print('A')
else:
    print('N')
