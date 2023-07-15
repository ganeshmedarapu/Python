def Reverse(s):
    if len(s)==0 or len(s)==1:
        return s
    return Reverse(s[1:])+s[0]
s=input('Enter any string:')
print(Reverse(s))