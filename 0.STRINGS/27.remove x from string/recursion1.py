def removeX(s,x):
    if len(s)==0:
        return s
    if s[0]==x:
        return removeX(s[1:],'x')
    else:
        return s[0]+removeX(s[1:],'x')
print(removeX('cxgfsgcx','x'))
