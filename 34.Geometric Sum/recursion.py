def Geometric_sum(k):
    if k==0:
        return 1
    return 1/(pow(2,k)) + Geometric_sum(k-1)
print(Geometric_sum(3))