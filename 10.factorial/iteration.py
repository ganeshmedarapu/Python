n=int(input('Enter a number: '))
fact=1
if n<0:
    print('Invalid Number')
else:
    for i in range(1,n+1):
        fact*=i
print(fact)