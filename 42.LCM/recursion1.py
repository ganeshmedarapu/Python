def hcf(dividend,divisor):
    remainder=dividend%divisor
    if remainder==0:
        return divisor
    return hcf(divisor,remainder)
def lcm(dividend,divisor):
    return (dividend*divisor)//hcf(dividend,divisor)
print(lcm(4,2))