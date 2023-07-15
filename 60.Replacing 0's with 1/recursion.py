n=int(input('Enter any number:'))
s=str(n)

def Replacing(s):
    if len(s)==0:
        return s
    if s[0]=='0':
        return '1'+Replacing(s[1:])
    else:
        return s[0]+Replacing(s[1:])
print(Replacing(s))






