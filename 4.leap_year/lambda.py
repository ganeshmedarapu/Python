n=int(input('Enter an year: '))
res=lambda n:'L' if n%400==0 or n%4==0 and n%100!=0 else 'N'
print(res(n))