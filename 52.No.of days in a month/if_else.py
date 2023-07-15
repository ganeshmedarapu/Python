month = int(input('Enter month:'))
year = int(input('Enter year:'))
days_31 = [1,3,5,7,8,10,12]
days_30 = [4,6,9,11]
if month in days_31:
    print('31')
elif month in days_30:
    print('30')
elif year%400==0 or year%4==0 and year%100!=0:
    print('29')
else:
    print('28')
