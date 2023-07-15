n=int(input('Enter any number:'))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=",")

'''
Approach 1 using while loop

n=int(input('Enter any number:'))
i=1
while i<=n:
    if n%i==0:
        print(i,end=",")
    i+=1'''

