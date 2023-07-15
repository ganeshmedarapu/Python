def isPrime(n,i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return isPrime(n,i+1)
n=int(input('Enter n value: '))
if isPrime(n):
    print('Prime')
else:
    print('Not Prime')










