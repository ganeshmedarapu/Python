n=int(input("Enter any number:"))
temp=n
sum=0
fact=1
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
while temp!=0: 
    remainder = temp%10 
    sum+=fact(remainder)
    temp=temp//10 
if sum==n:
    print("Strong Number")
else:
    print("Not a strong Number")


''' Approach 1 using inbuilt function

import math
n=int(input("Enter any number:"))
temp=n
sum=0
while temp!=0: 
    remainder = temp%10 
    sum+=math.factorial(remainder)
    temp=temp//10 
if sum==n:
    print("Strong Number")
else:
    print("Not a strong Number")'''
    
