a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(a,b))