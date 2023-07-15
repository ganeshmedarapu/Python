n=int(input('Enter any number:'))
n1=n-1
def Handshakes(n1):
    if n1==0:
        return 0
    return n1+Handshakes(n1-1)
print(Handshakes(n1))




''' Approach 1-Using for loop

sum=0
for i in range(1,n):
    sum+=i
print(sum)'''




''' Approach 2-Using while loop

i=1
sum=0
while i<n:
    sum+=i
    i+=1
print(sum)'''

    



