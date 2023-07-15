def removeDup(s):
    if len(s)==0 or len(s)==1:
        return s
    smallOutput=removeDup(s[1:])
    if s[0]==smallOutput[0]:
        return smallOutput
    else:
        return s[0]+smallOutput
print(removeDup('xxxyyyxushgxxx'))