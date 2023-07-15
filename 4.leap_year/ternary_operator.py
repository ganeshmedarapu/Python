n=int(input('Enter an year: '))
print('L' if n%400==0 or n%4==0 and n%100!=0 else 'N')