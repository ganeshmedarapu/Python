def hcf(a,b):
    if a%b==0:
        return b
    return hcf(b,a%b)
print(hcf(4,2))