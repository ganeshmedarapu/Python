def Pair_Star(s):
    if len(s)==0 or len(s)==1:
        return s
    y=Pair_Star(s[1:])
    if s[0]==y[0]:
        return s[0]+'*'+y
    return s[0]+y
s='aaabbb'
print(Pair_Star(s))
    