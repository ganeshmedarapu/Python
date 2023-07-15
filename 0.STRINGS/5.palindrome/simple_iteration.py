from math import *
n=int(input('Enter a number: '))
temp=n
rev=0
while temp>0:
    remainder=temp%10
    rev=(rev*10)+remainder
    temp//=10
if n==rev:
    print('P')
else:
    print('N')
