def CountZeros(n):
    if n==0:
        return 0
    if n%10==0:
        return 1+CountZeros(n//10)
    return CountZeros(n//10)
print(CountZeros(10000))
    