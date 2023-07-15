n=int(input())
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print('p' if isprime(n) else 'n')