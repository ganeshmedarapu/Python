n=int(input('Enter an year: '))
if n%400==0 or n%4==0 and n%100!=0:
    print('L')
else:
    print('N')