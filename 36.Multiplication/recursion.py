def Multiplication(m,n):
    if m==0 or n==0:
        return 0
    return m+Multiplication(m,n-1)
print(Multiplication(3,5))
