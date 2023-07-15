def no_vowels(s):
    if s=='':
        return 0
    if s[0]=='a' or s[0]=='e' or s[0]=='i' or s[0]=='o' or s[0]=='u':
        return 1+no_vowels(s[1:])
    return no_vowels(s[1:])
print(no_vowels('Haii'))