def hcf(dividend,divisor):
    remainder=dividend%divisor
    if remainder==0:
        return divisor
    return hcf(divisor,remainder)
print(hcf(4,2))