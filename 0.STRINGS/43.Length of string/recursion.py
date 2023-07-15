def len_str(s):
    if s=='':
        return 0
    return 1+len_str(s[1:])
print(len_str('Ganesh'))