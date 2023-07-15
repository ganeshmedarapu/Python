def replaceChar(s,a,b):
    if len(s)==0:
        return s
    if s[0]==a:
        return b+replaceChar(s[1:],a,b)
    else:
        return s[0]+replaceChar(s[1:],a,b)
print(replaceChar('www','w','x'))