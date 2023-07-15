n=int(input('Enter a number: '))
flag=0
for i in range(2,n):     #for i in range(2,int((n/2)+1))    we can optimize by taking (n/2)+1
    if n%i==0:
        flag=1
        #break             #also we can optimize by using break
if flag==1:
    print('Not prime')
else:
    print('Prime')
    