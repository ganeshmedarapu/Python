def Sum_of_digits(n):
    if n==0:
        return 0
    return (n%10)+Sum_of_digits(n//10)
print(Sum_of_digits(12345))