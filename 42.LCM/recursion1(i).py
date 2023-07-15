def hcf(a,b):
    if a%b==0:
        return b
    return hcf(b,a%b)
def lcm(a,b):
    return (a*b)//hcf(a,b)
print(lcm(4,2))