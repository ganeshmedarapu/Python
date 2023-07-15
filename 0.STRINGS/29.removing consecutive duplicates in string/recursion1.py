def removeDup(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]==removeDup(s[1:])[0]:
        return removeDup(s[1:])
    else:
        return s[0]+removeDup(s[1:])
print(removeDup('xxxyyyxushgxxx'))