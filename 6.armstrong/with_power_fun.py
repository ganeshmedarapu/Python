n=int(input('Enter a number: '))
l=len(str(n))
temp=str(n)
sum=0
for i in temp:
    sum=sum+int(i)**l    #sum=sum+pow(int(i),l)
if n==sum:
    print('A')
else:
    print('N') 