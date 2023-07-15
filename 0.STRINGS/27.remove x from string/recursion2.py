def removeX(s,x):
    if len(s)==0:
        return s
    smallOutput=removeX(s[1:],'x')
    if s[0]==x:
        return smallOutput
    else:
        return s[0]+smallOutput
print(removeX('abcx','x'))