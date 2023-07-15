s=input('Enter a word: ')
j=-1
flag=0
for i in s:
    if i!=s[j]:
        flag=1
        break
    j-=1
if flag==1:
    print('N')
else:
    print('P')