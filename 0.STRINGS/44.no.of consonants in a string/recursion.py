def no_cons(s):
    if s=='':
        return 0
    if s[0]!='a' and s[0]!='e' and s[0]!='i' and s[0]!='o' and s[0]!='u':
        return 1+no_cons(s[1:])
    return no_cons(s[1:])
print(no_cons('Ganesh'))